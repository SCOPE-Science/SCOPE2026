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
The proof was reconstructed from the semidirect-product multiplication law and the definition of subgroup commutativity degree.

Critical symbolic checks:
- every subgroup outside an odd abelian kernel is uniquely \(H(B,x)=B\rtimes\langle xt\rangle\) for \(B\le A\) and \(x+B\in A/B\);
- every \(B\le A\) is normal in the generalized dihedral group;
- for \(H(B,x)\) and \(H(C,y)\), direct multiplication gives \(HK=KH\) exactly when \(x-y\in B+C\);
- the odd-order condition is used precisely to exclude a nonzero order-two class in \(A/(B+C)\);
- the number of compatible ordered coset pairs for fixed \(B,C\) is \(|A:B\cap C|\);
- for \(A=(C_p)^r\), the displayed Gaussian-binomial sum counts subspace pairs by \((\dim B,\dim C,\dim(B\cap C))\);
- the leading exponent in an \(\eta_r(p)\) summand is
  \[
  r+a(r-k-a)+b(r-k-b)+k(r-k-1),
  \]
  whose global maximum occurs at \(k=0\), yielding one leading term in even rank and three in odd rank.

The packaged `artifacts/verify.py` directly constructs all classified subgroups for \(C_3\), \(C_5\), \(C_9\), and \(C_3\times C_3\), tests \(HK=KH\) for every ordered subgroup pair, and checks the formula against the direct count. It also evaluates the Gaussian-binomial specialization and the rank-one closed form. The replay returns `VERIFY_OK`.

Finite computation is not used to establish the universal formula or the asymptotic statements.
