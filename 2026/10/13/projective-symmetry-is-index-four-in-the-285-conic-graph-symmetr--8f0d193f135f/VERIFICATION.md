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
# Verification

The finite calculation in `verify.py` uses only the displayed transcendental lattice \(T=\langle6\rangle\oplus\langle20\rangle\) and the source value \(|O_h(N)|=2880\). It enumerates the discriminant group \(A_T\cong\mathbb Z/6\oplus\mathbb Z/20\), preserving the quadratic form \(q_T(a,b)=a^2/6+b^2/20\pmod{2\mathbb Z}\), and obtains exactly eight automorphisms. It separately checks that the square-six vectors are only \(\pm e_1\), forcing \(O(T)\) to be the four diagonal sign changes and \(O^+(T)=\{\pm I\}\). The latter has discriminant image of order two.

The script therefore checks the exact arithmetic
\[
|\ker(O_h(N)\to O(q_N))|=2880/8=360,
\qquad
|\operatorname{Aut}_{\mathbb P^4}(X_{285})|=360\cdot2=720.
\]

The script does not reconstruct Degtyarev's 285-vertex graph or reprove the published GAP computation \(|O_h(N)|=2880\); those are explicit source inputs. It also does not identify the abstract isomorphism type of the order-\(720\) group.
