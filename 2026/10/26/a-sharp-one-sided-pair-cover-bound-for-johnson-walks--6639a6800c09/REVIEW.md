# Self-review

**Correctness — PASS.** The exact transition kernel is obtained from mutually exclusive delete/insert cases. The killed-chain Perron eigenvector gives componentwise upper/lower survival estimates, which combine with the union bound and a geometric tail to give the finite and asymptotic cover-time upper bounds. A standalone exact-rational finite replay checks the nontrivial lumping and initial weights. The argument does not purport to show a matching cover-time lower bound.

**Originality — PASS on inspected evidence, subject to historical-priority risk.** Athreya–Mukherjee–Mukherjee, arXiv:2304.01145, state the broader Markovian conjecture and solve \(r=s\), while their independent-sampling first-moment theorem has no dependence. The presented fixed-pair killed eigenvalue and sharp dependent \(s=2<r\) upper bound were not found among inspected results or comparison searches. General graph cover-time estimates and other Johnson-slice spectral results concern distinct quantities; an undiscovered general set-hitting theorem could subsume the upper bound.

**Value — PASS.** The upper limit resolves one side of the leading-constant assertion in an explicit open Markovian coupon-collection conjecture, and the finite-sample survival envelope plus critical-window mean profile provide useful exact quantitative statements even without a matching lower bound. The structural reduction to a two-state killed chain retains long-range temporal dependence rather than assuming independent rounds.

Closest source: S. Athreya, S. Mukherjee and S. S. Mukherjee, *On a Generalisation of the Coupon Collector Problem*, arXiv:2304.01145, §§2–3. Relevant general comparison: Rivera, Sauerwald and Sylvester, *Multiple random walks on graphs: mixing few to cover many* (2023). Unresolved: the matching lower bound, a Gumbel law, joint survival for pairs and possible implicit earlier general hitting-set bounds.

Self-review: passed. Independent audit: not yet performed.
