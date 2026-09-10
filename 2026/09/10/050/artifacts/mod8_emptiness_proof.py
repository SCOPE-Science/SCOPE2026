"""Certificate: U_3(Z/8) empty and affine E1(Z/8) empty.
F3(x,y,z) = x^2+y^2+z^2+4(sum x^2y^2)-16x^2y^2z^2-3, k=3.
E1aff(x,y) = 5x^2+5y^2-12x^2y^2-2 (z=1 fibre).
Exhaustive check over all residue classes (512 and 64).
Replay: python3 mod8_emptiness_proof.py -> PROOF_OK.
Stdlib only.
"""
def F3m(x, y, z, k=3):
    return x * x + y * y + z * z + 4 * (x * x * y * y + y * y * z * z + z * z * x * x) - 16 * x * x * y * y * z * z - k

def E1m(x, y):
    return 5 * x * x + 5 * y * y - 12 * x * x * y * y - 2

def main():
    sols = [(x, y, z) for x in range(8) for y in range(8) for z in range(8) if F3m(x, y, z) % 8 == 0]
    aff = [(x, y) for x in range(8) for y in range(8) if E1m(x, y) % 8 == 0]
    print("U_3 mod8 solutions:", len(sols))
    print("E1 affine mod8 solutions:", len(aff))
    assert len(sols) == 0, sols[:10]
    assert len(aff) == 0, aff[:10]
    print("PROOF_OK: U_3(Z/8) empty and E1_aff(Z/8) empty")

if __name__ == "__main__":
    main()
