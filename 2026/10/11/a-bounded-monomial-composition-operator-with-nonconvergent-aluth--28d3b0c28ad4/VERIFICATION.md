---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

With s_j=(-1)^floor(log2(j+1)) and F(0)=0 of slopes s_j, F is 1-Lipschitz, |F(t)|<=t. Thus beta(0)=1, n^-1<=beta(n)=2^[F(log2 n)]<=n, beta(n)^(1/n)->1, and n/(n+1)<=beta(n+1)/beta(n)<=(n+1)/n. Polynomial coefficient weights make H2(beta) analytic; C_z2 maps orthonormal e_n to d_n e_(2n) with d_n=beta(2n)/beta(n) in [1/2,2]; d_1=2 gives ||C_z2||=2. The span of e_(2^j), j>=0, is reducing for T and T*, supporting a unilateral positive shift with w_j=2^s_j; no off-orbit monomial maps onto it. For any positive shift, polar decomposition yields Delta weights sqrt(w_j w_(j+1)), and induction gives first coefficient b_N=2^[2^-N sum_{j=0}^N binom(N,j)s_j]. At N=3*2^ell, the Bin(N,1/2) mean is 3*2^(ell-1); the event |B-N/2|<2^(ell-2) lies wholly in j in [2^ell-1,2^(ell+1)-2], where s_j=(-1)^ell. Hoeffding bounds the complement by 2 exp(-2^ell/24), hence |E s_B-(-1)^ell|<=4exp(-2^ell/24), so b_N tends to 2 on even ell and 1/2 on odd ell. A fixed WOT coefficient diverges, disproving SOT convergence without finite-to-infinite extrapolation. Independent exact-rational binomial computations for ell=4..10 corroborated the formula and estimate; the infinite conclusion uses the analytic proof.

## originality

PASS

Compared the exact analytic composition statement and its quantifiers, not just its title, to Chō–Jung–Lee 2005 abstract weighted shifts, Lahiri–Ojha–Birbonshi 2026 Questions 5.1/5.2, Jung–Kim–Ko 2015 two fractional symbols, Benhida–Budzyński–Trepkowski 2018 L2 theory and Chalendar–Partington 2020 power iterates. The shift divergence and binomial formula are known, but the exact regular weighted-Hardy analytic realization by unweighted C_(z^2) is an additional demonstrated fact not implied without embedding. Resultary exact same-ID hit is this finding itself, not a distinct earlier publication. This is best-of-knowledge priority, with the inaccessible 2015 full text and possible unindexed realization explicitly retained as risks.

## value

PASS

This explicit counterexample settles the published universal composition-operator Aluthge convergence question (Lahiri–Ojha–Birbonshi 2026, Q5.2) negatively, while preserving important analytic structure: fixed elementary z^2 symbol, bounded multiplication by z, coefficient weights between n^-1 and n with neighbor ratios tending to one. Such a boundary distinguishes restricted linear-fractional positive results from arbitrary weighted Hardy spaces. The exact realization matters to researchers delimiting hypotheses for future positive convergence theorems; this is not merely relabeling abstract shift nonconvergence or claiming the 2005 mechanism itself as new. It does not address classical Hardy, weighted Bergman, nor Question 5.1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
