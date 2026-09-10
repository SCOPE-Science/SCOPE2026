"""Master replay: runs every verification-critical script.
Usage: python3 output/artifacts/replay_all.py
Each sub-check prints its own transcript; this driver asserts all pass.
Covers: join diameter (=pi), factor isometry, link volume (pi*a),
link diameter (pi), volume scaling (4pi*a/3), radius/topology diagnostics,
eccentricity profile + radius.
NOTE: check_packing_bound.py is intentionally NOT copied here: it documents
its own retraction (Bishop-Gromov sign error) and is NOT cited as evidence.
"""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = [
    "check_join_diameter.py",
    "check_factor_isometry.py",
    "check_link_volume.py",
    "check_link_diameter.py",
    "check_volume_collapse.py",
    "check_radius_and_topology.py",
    "check_eccentricity.py",
]

fails = []
for s in SCRIPTS:
    p = os.path.join(HERE, s)
    print(f"===== {s} =====")
    r = subprocess.run([sys.executable, p], capture_output=True, text=True)
    print(r.stdout, end="")
    if r.stderr:
        print("--- stderr ---")
        print(r.stderr, end="")
    print(f"exit={r.returncode}")
    if r.returncode != 0:
        fails.append(s)

if fails:
    print(f"REPLAY FAIL: {fails}")
    sys.exit(1)
print("REPLAY_ALL PASS: every target-audit computation replays.")
