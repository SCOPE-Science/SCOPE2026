# Same-model review

## Correctness
PASS. If the current rejection count is \(r>0\), every old rejected e-value is at least \(c_r=K/(\alpha r)\). Keeping those same coordinates above \(c_r\) makes the next \(r\)-th order statistic at least \(c_r\), so the next e-BH rejection count is at least \(r\) and its cutoff is no larger than \(c_r\). The one-coordinate counterexample proves sharpness. The lock-and-bet update is a nonnegative supermartingale step because its conditional expectation is at most the current e-value whenever the one-step factor has conditional null mean at most one.

## Originality
PASS, with a residual terminology/indexing risk. The recent adaptive-sampling source proves nested rejection sets under a sufficient policy that samples only currently unrejected hypotheses. Base e-BH supplies the rank cutoff but not a prospective post-rejection continuation rule. The carefree multiple-testing paper handles revocation using running suprema and adjusters, rather than by locking the current e-BH threshold inside each rejected e-process. The stopped e-BH paper addresses the global-filtration condition. Targeted semantic searches did not reveal the cutoff-locking lemma, its sharp one-coordinate obstruction, or the maximal-active-capital corollary.

## Value
PASS. The result relaxes a concrete restriction in a new adaptive multiple-testing procedure: an already rejected hypothesis need not become permanently unsampleable. The theorem gives an exact amount of evidence that must be protected, allows any surplus to keep accumulating information, and shows that the protected amount is worst-case minimal. Because additional discoveries lower the e-BH cutoff, the rule also yields an explicit mechanism for progressively releasing locked evidence.

## Closest literature and limitations
The closest recent source is Lin–Ma–Ren–Wei, arXiv:2609.26651v1. Foundational e-BH is Wang–Ramdas, DOI 10.1111/rssb.12489. The closest alternative treatment of revocation is Tavyrikov–Goeman–de Heide, DOI 10.1214/26-EJS2546, and the filtration caveat is treated by Wang–Dandapanthula–Ramdas, DOI 10.1016/j.spl.2025.110512. The claim is limited to base e-BH, pathwise coordinatewise persistence, and globally valid sequential factors. It does not claim optimality for power, expected stopping time, or adaptive allocation.

Same-model review: passed. Independent audit: not yet performed.
