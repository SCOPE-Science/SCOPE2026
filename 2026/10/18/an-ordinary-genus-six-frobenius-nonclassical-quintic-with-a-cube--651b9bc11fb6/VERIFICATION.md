---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The final theorem is for precisely the F4 plane quintic of Asgarli–Duan–Lai Example 4.10 with a²+a+1=0, and its q=4 zeta numerator. Recomputed F_X=(a+1)X⁴+X²Y²+X²YZ+X²Z²+Y⁴+Y²Z²+Z⁴, F_Y=Z(X³+Z³), F_Z=Y(X³+Y³). Their simultaneous projective zeros must be among 16 points defined over F4: one [1:0:0], three [x:1:0], twelve [x:y:1]. Independent F4 arithmetic excludes all, establishing geometric smoothness and genus g=6. On Z=1 the equation is an F2-linearized polynomial in Y with coefficients depending on X; independent exact polynomial-basis field arithmetic and rank-of-linear-map counts give N1..N7=(5,35,65,395,1025,3395,16385). For m=1..6, p_m=4^m+1−N_m=(0,−18,0,−138,0,702). Newton identities produce c_0..c_6=(1,0,9,0,75,0,315), and functional equation c_{12−i}=4^{6−i} c_i completes L_C(T)=(1+3T²+16T⁴)^3. Degree-six mod-2 L implies full p-rank 6 and ordinarity; P(U)=U⁴+3U²+16 is irreducible over Q and ordinary, so standard Honda–Tate/Tate produce J~A³ with A a simple ordinary surface. Under F16 base change P maps to (U²+3U+16)², hence J~E⁶ with trace −3. Opposite-sign roots imply N_{odd}=4^n+1; for n=2k the squared roots give recurrence s0=2,s1=−3,s_k=−3s_{k−1}−16s_{k−2} and N_{2k}=16^k+1−6s_k. Isogeny is not polarized isomorphism. Exact finite checks corroborate the analytic derivation; no finite enumeration is misrepresented as an all-n proof.

## originality

PASS

Best-of-knowledge originality of the complete Weil numerator of this specific previously published plane quintic: the identical defining source supplies the equation and geometric features but not its extension-field zeta polynomial. The quoted Hefez–Voloch count gives only N_1. Independently obtained N_2,...,N_6 uniquely supply the new numerator via Newton identities and functional equation, from which standard isogeny theorems apply. No inspected exact prior statement, stronger implication, or same-curve table covers it; residual bibliographic priority risks remain.

## value

PASS

The special curve is an established geometrically natural Frobenius-nonclassical plane quintic, not an arbitrary sampled coefficient choice. Determining its exact zeta numerator and ordinarity identifies a concrete genus-six Jacobian as a third power of a simple abelian surface over F4 and a sixth power of an ordinary elliptic curve over F16; the all-odd-extension vanishing Frobenius trace and even-extension recurrence are nontrivial structural arithmetic consequences. The exact invariant of this named curve is independently useful in future arithmetic, point-count, isogeny and special-geometry comparisons. Classical Newton and Honda–Tate steps are appropriately credited, and no larger family classification or external certification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
