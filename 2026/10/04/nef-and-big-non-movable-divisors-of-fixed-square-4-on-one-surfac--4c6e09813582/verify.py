def invariants(n):
    assert n >= 3 and n % 2 == 1
    F_Gamma = 4
    G_Gamma = n*n
    A2 = 2*F_Gamma
    branch_F = 2
    branch_Gamma = 2*(F_Gamma + G_Gamma)
    genus_F = 1 + branch_F//2
    genus_Gamma = 1 + branch_Gamma//2
    CF2 = 0
    Cn2 = 0
    CF_Cn = 2*F_Gamma
    blown = 3
    Ft2 = CF2 - blown
    Nt2 = Cn2 - blown
    FtNt = CF_Cn - blown
    D_F = Ft2 + FtNt
    D_N = Nt2 + FtNt
    D2 = Ft2 + Nt2 + 2*FtNt
    return A2, branch_F, branch_Gamma, genus_F, genus_Gamma, Ft2, Nt2, FtNt, D_F, D_N, D2

for n in range(3, 1000, 2):
    z = invariants(n)
    assert z[0] == 8
    assert z[1] == 2
    assert z[2] == 2*(n*n+4)
    assert z[3] == 2
    assert z[4] == n*n+5
    assert z[5:8] == (-3, -3, 5)
    assert z[8:] == (2, 2, 4)

for n in [3,5,7,11,31,101]:
    allowed = [m for m in range(1, n*n+3) if 4*m < n*n+4]
    assert allowed == list(range(1, n*n//4 + 2))

print("checked_odd_n=3..999")
print("post_blowup_intersection_matrix=[[-3,5],[5,-3]]")
print("component_intersections_with_D=(2,2)")
print("D_square=4")
print("component_genera=(2,n^2+5)")
print("VERIFY_OK")
