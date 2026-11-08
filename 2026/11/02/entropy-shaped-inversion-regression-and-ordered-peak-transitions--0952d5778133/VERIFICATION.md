---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

In a signed full binary tree each internal node is canonically assigned to a gap between its left/right leaf subtrees, whose two subtree sizes L_k,R_k count exactly the cross-subtree pairs. A pair is inverted iff its lowest common ancestor is negatively signed. Since random leaf splits do not inspect signs, B_k are iid Bernoulli(q), independent of unsigned tree, and I_n=sum B_k L_kR_k. Yule uniform-leaf splits induce the uniform-root-split BST recursion; independent priorities for all n-1 gaps generate it. Given priority U_k=t, nearest smaller priorities on each side give independent geometric tails, and E[L_kR_k|t]=(1-(1-t)^k)(1-(1-t)^(n-k))/t^2. Integrating yields w_nk=nH_{n-1}-kH_{k-1}-(n-k)H_{n-k-1}-1, including w_2,1=1. Differences w_(k+1)-w_k=H_(n-k-1)-H_k yield symmetry/strict concavity, hence strict log-concavity and increasing peak thresholds. Since P_i=(1-B_(i-1))*B_i, independence gives Cov(I,P_i)=pq*(p*w_i-q*w_(i-1)). Sum w=binom(n,2) gives E[I|D=d]=nd/2; harmonic asymptotic gives w_(floor alpha n)/n->binary entropy, fixed k gives k log n+O(1); so first and last peak thresholds ->1/3,2/3 while bulk ->1/2. All boundary n and peak ranges checked, no finite enumeration substituted for general proof.

## originality

PASS

Féray--Rivera-Lopez define precisely this recursive model, signed tree, full point probabilities and total-descent Bernoulli distribution; these are treated as prior. The new evaluated L_kR_k positional kernel, full descent-vector inversion regression and ordered peak thresholds are not stated or implied without a nontrivial BST priority calculation. Chen--Kitaev--Zhang work is for uniform separable measure, not this recursive biased law. Resultary nearby uniform permutation inversion/cycle-covariance results are different.

## value

PASS

The exact influence of a local descent on global inversions is nonuniform: logarithmic near edges, order n with binary entropy envelope in bulk. Combined with the ordered peak-covariance sign transitions, this is a natural complete local-global statistic dependence classification for a nonuniform recursive separable permutation measure, beyond mere known binomial total descents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
