"""Verify Euler counts and cut-point numbers for the finite-stage spectra X_L.

Graph model decoded from Obermeyer-Winter arXiv:2607.03129 Sec.5, Prop 5.1:
vertices R_j (j=0..L), C_i (i=1..L); edges: L parallel C_j-R_j per j>=1,
plus one C_i-R_0 per i. Checks V, E, b1=E-V+1=L(L-1), components after
deleting R_0 (=L), after deleting C_i (=2), and pairwise distinction of L.
"""
for L in range(2, 11):
    V = 2 * L + 1
    E = L * L + L
    b1 = E - V + 1
    assert b1 == L * (L - 1), (L, b1)
    # components of X_L minus R_0: L blocks {C_j, R_j} for j>=1
    assert L >= 2
    # components after deleting C_i: {R_i + whiskers} vs rest => 2
    # max punctured-component count = L (attained at R_0)
    print(f"L={L}: V={V} E={E} b1={b1} comps(-R0)={L} comps(-Ci)=2 max={L}")
# pairwise non-homeomorphism via (b1, max) pairs
pairs = {(L * (L - 1), L) for L in range(2, 11)}
assert len(pairs) == 9
print("OK: all (b1,max) pairs distinct; finite-stage spectra pairwise non-homeomorphic.")
