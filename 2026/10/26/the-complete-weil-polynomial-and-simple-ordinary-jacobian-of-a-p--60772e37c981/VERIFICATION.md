---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification

The checked equation over \(\mathbb F_3\) is \(X^5Y+X^5Z-X^3Y^3+X^3Z^3+XZ^5+Y^5Z-Y^3Z^3=0\).

1. Compile and run `g++ -O3 -std=c++17 verify.cpp -o check && ./check` from the directory containing the two source files. The program constructs explicit fields of orders \(3^m\) for \(1\le m\le10\), validates multiplicative periods and exhaustive field traversal, computes \(\deg\gcd_y(f_x,y^{3^m}-y)\) for every \(x\), adds the four points at infinity, and prints every exact point count. For \(m\le5\) it also directly enumerates all affine pairs to cross-check the gcd computation. Its successful final marker is `VERIFY_OK`.
2. Run `python3 check_arithmetic.py`. The script checks the reduction identity at the affine singular locus and \(\gcd(G,R)=1\) in characteristic three. It computes the twenty-one Weil coefficients from the point counts, checks \(\deg L=20\) and \(c_{10}
ot\equiv0\pmod3\), and performs the exact Rabin irreducibility test modulo \(23\). Its final marker is `VERIFY_ARITHMETIC_OK`.

The finite point counts through degree ten are exhaustive computations, not randomly sampled values. The conclusion for all extension degrees also uses the smooth genus-ten Weil functional equation and Newton identities. Irreducibility over \(\mathbb Q\) follows from the modular irreducibility certificate; geometric absolute simplicity is not tested or claimed. Independent audit and validation have not been performed.
