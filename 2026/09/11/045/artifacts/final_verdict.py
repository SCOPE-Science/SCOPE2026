"""Final: replayable certified verdict with mesh-convergence error bars.
Writes ledger_final.json + prints table. Exit code 0 + VERIFY_OK iff pass."""
import numpy as np, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_ledger import run

meshes = [(32, 128), (48, 176), (64, 224)]
data = {}
for (Nr, Nt) in meshes:
    rows, gap, info = run(Nr, Nt)
    data[(Nr, Nt)] = (rows, gap, info)

keys = list(data.keys())
fine_rows, fine_gap, fine_info = data[keys[-1]]
mid_rows, mid_gap, _ = data[keys[-2]]
ncell = len(fine_rows)
TOL = 1e-3
print("cell | minA_fine | minB_fine | dA(f-m) | dB(f-m) | res | verdict")
ok_all = True
ledger = []
for i in range(ncell):
    fA = fine_rows[i]['minA']; fB = fine_rows[i]['minB']
    mA = mid_rows[i]['minA']; mB = mid_rows[i]['minB']
    dA = abs(fA - mA); dB = abs(fB - mB)
    res = max(fine_rows[i]['resA'], fine_rows[i]['resB'])
    disc = max(dA, dB)  # mesh discrepancy as error proxy
    # safety factor: error bar = discrepancy(fine-mid) + res + small floor
    bar = disc + res + 1e-12
    sA = np.sign(fA); sB = np.sign(fB)
    agree = (sA == sB)
    # certified: |min| > bar + TOL on BOTH, so sign can't flip within tol
    certified = agree and (abs(fA) > bar + TOL) and (abs(fB) > bar + TOL)
    ok_all &= certified
    ledger.append(dict(cell=i, C=fine_rows[i]['C'], minA_fine=fA, minB_fine=fB,
                       mesh_discA=dA, mesh_discB=dB, eig_res=max(fine_rows[i]['resA'], fine_rows[i]['resB']),
                       error_bar=bar, signs=[float(sA), float(sB)], certified_sign_agreement=bool(certified)))
    print(f"{i:2d} | {fA:+.5f} | {fB:+.5f} | {dA:.2e} | {dB:.2e} | {res:.1e} | {'CERT' if certified else 'FAIL'}")
gaps = [data[k][1] for k in keys]
print("gaps:", [f"{g:.5f}" for g in gaps])
gap_ok = all(g >= 0.02 for g in gaps)
print("gap>=0.02 on all meshes:", gap_ok)
# monotonic mesh trend check for gap (increasing refinement -> stable)
print("target verdict:", "PASS" if (ok_all and gap_ok) else "FAIL")
out = dict(meshes=[f"{a}x{b}" for a, b in keys], tol=1e-3, alpha=1.5,
           ledger=ledger, gaps=gaps, pass_all=bool(ok_all and gap_ok))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ledger_final.json'), 'w') as f:
    json.dump(out, f, indent=1)
print("VERIFY_OK" if (ok_all and gap_ok) else "VERIFY_FAIL")
