---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On mean-zero vertex potentials the Laplacian eigenvalues are D=n-2+2c in the e_1-e_2 direction and n orthogonally. For the unit ordinary-edge injection e_1-e_3 the potentials are (1/(2n)+1/(2D), 1/(2n)-1/(2D), -1/n, 0, ...). Summing their absolute differences with multiplier t=sqrt(c) at edge {1,2} gives A_n; the second potential changes sign at c=1, while its difference from the third is (n-3+3c)/(nD)>0 in both ranges. Exceptional injection acts in the D-eigendirection and gives the diagonal 2c/D and 2(n-2) entries of magnitude t/D. For a remote edge the injection is in the n-eigenspace, so its row is unweighted. No remote row exists at n=3. The row-sum characterization on the full real edge space follows by aligning the edge input signs with a maximizing row. Write M=(1+sqrt(2n-3))/2, so n-2=2M(M-1). Then D(M-E_n)=2(M-1)(t-M)^2. For 0<t<=1 the adjacent row is 1+(n-3+t)/D<2; to handle n=3,4,5, its bounds are respectively 1+1/(2sqrt(2)), 1+(1+sqrt(2))/4, and 9/5, all below M. For n=5 the last bound follows from 8t^2-5t+2>0. For t>=1 the factorization of A_n-R_n shows A_n<=R_n for t>=(n-2)/2; on 1<=t<=(n-2)/2 the factorization of E_n-A_n gives a nonnegative difference since the bracket is at least n(n-2). The numerical quantity R_n<M even for n=3, where it is only a comparison constant. Thus the full norm reaches M at c=M^2. Orientations conjugate by a diagonal sign matrix and do not affect the norm.

## originality

PASS

Credit the earlier balanced complete-bipartite exceptional-edge result for the same general rank-one entry update and optimization of an exceptional row in that model. Substitution of the unweighted clique entries gives the exceptional row and its extremum by the same method. The distinct claim assessed here is the exact full induced norm on the one-edge weighted clique, including the sign-sensitive adjacent rows and proof that no row in any conductance range or graph order n>=3 exceeds the exceptional peak. The inspected analogue and general routing bounds do not establish this conclusion.

## value

PASS

The graph and norm are natural: the unweighted clique has a uniform bound below two, yet a single varied conductance in symmetric electrical-gradient coordinates produces a sharp order-sqrt(n) norm. Exact determination of all row families and the optimizer shows which responses can dominate and is meaningful for comparing endpoint amplification between symmetric network families; generic perturbation entries or a universal growth estimate are not an adequate substitute. The analogous complete-bipartite mechanism is already known, so the value is the exact clique result, not discovery of the general amplification mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
