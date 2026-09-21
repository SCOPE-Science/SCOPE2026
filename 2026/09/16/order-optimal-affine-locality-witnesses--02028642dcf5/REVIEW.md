# same-model review

## Correctness: PASS

The graph construction is explicit over \(\mathbb F_q\). Degree counts,
bipartition, connectedness, and the absence of 3- and 4-cycles are checked
directly from affine-line incidence. The cross-edge set is an efficient edge
dominating set, so Cardoso et al., Theorems 2.1 and 3.1, certify its maximum
induced-matching size. The set \(A\) is a total perfect code; the girth-six
argument converts that property into the exact one-addition and one-for-two
local-optimality predicate. The order lower bound follows from the independently
inspected local-search bound of Fürst--Leichter--Rautenbach, Theorem 5, the
regular conflict-set upper bound, and the coprimality calculation.

The computational evidence is independently constructed rather than a check of
the displayed formulas: `affine_locality_check.py` tests the raw graph, and for
q=3 exhaustively computes the optimum. It also includes a negative control
showing that dropping the girth restriction can permit an exchange.

## Equivalence And Coverage: PASS

The claim was rewritten in four equivalent forms during the audit:

1. an induced matching stable under 1-add and 1-for-2 exchange;
2. an independent set in the square of the line graph stable under the analogous
   exchange;
3. a q-regular girth-six graph attaining equality in both
   \(|M|\ge m/q^2\) and \(\nu_s\le m/(2q-1)\);
4. simultaneous existence of a total perfect code whose induced edges are
   \(M\), and an efficient edge dominating set of size \(q^2\).

The primary sources inspected settle only the component inequalities. Fürst--
Leichter--Rautenbach, Theorem 5 and Corollary 6(ii), do not construct a
minimum-order simultaneous certificate. Cardoso et al., Theorems 2.1 and 3.1,
show that the efficient edge dominating certificate is maximum but do not impose
the total-perfect-code certificate or the affine order. The newest inspected
primary paper, Grippo--Lin--Vera, arXiv:2509.04598v2 / DOI
`10.1016/j.tcs.2026.116142`, defines DIMs and PED-sets and studies their
complexity; its Section 2 and stated results likewise contain no simultaneous
girth-six minimum-order construction.

The unrestricted arbitrarily-large-girth version was rejected as routine after
inspection of Neumann, arXiv:0906.2496, which states Leighton's common finite-cover
theorem. That theorem combines regular certificate graphs but supplies no
minimum-order result. The present affine construction is not obtained by that
cover argument and meets the lower bound exactly.

The Gotthilf--Lewenstein 2006 chapter remains inaccessible through the full-text
service. Its indexed abstract concerns approximation ratios; the accessible
primary reconstruction in Fürst--Leichter--Rautenbach, Corollary 3, identifies
the result recovered from it as an approximation guarantee, not a theorem about
simultaneous total perfect codes, girth six, or minimum order. No specific
covering theorem for the exact target was found in the inspected primary
literature. This is recorded as an access limitation, not as evidence that the
entire subject is uncovered.

## Value: PASS

The result identifies exact smallest witnesses for the worst-case local-search
ratio across an infinite prime-power degree family. It supplies finite benchmark
instances of order \(2q(2q-1)\), rather than unspecified common covers whose
orders can be arbitrarily large. The simultaneous total-perfect-code and DIM
certificates make the optimum and local failure independently checkable. This
is a structural extremal result, not a parameter relabeling or a routine
specialization of either source theorem.

## Overall Verdict: PASS

This is a same-model assessment only and is not independent validation.

## Recorded review qualifications

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult REVIEW.md for search evidence and inaccessible sources. Publication is not peer review or a guarantee of priority.
