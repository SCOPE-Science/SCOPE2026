# Scientific review

## Correctness — PASS

The claim concerns all integer slopes \(q\ge2\) and the limit of growing cylinder depth \(n\). The proof establishes an exact avoidance generating function from a first-occurrence decomposition and derives a unique physical leading root in \([1-2q^{-n},1]\). Its uniform approximation \(\gamma_n(w)/q^{-n}=C_w(q^{-1})^{-1}+O_q(nq^{-n})\) controls every hole, including periodic exceptions. The number of words with least period \(r\) is at most \(q^r\), giving a uniform square-summable tail. For fixed \(r\), primitive-block counting and the finite-word overlap lemma give exactly \(a_q(r)\) contributions, each tending to \(q^{-2r}\). The full centered-variance limit follows by dominated summation and an \(O_q(n^2q^{-n})\) error. The same estimates establish the normalized period-allocation law. Exact finite avoidance enumeration, numeric root evaluation, and Möbius summation were independently exercised by `checker.py`, which returned `VERIFY_OK`; infinite quantifiers rely on the written proof.

## Originality — PASS, with stated priority risk

The closest article is Georgiou–Dettmann–Altmann, arXiv:1207.7000, especially its period-orbit formula, Markov-hole expansions and ensemble **mean** calculations. It establishes the mechanism and primitive-counting ingredients but does not state the asymptotic **variance** of normalized rates or the limiting distribution of least periods after weighting by squared centered deviations. The new argument needs a uniform-in-hole root approximation, an order-of-limits justification under the square-summable period bound, and explicit variance centering. Bonanno–Cristadoro–Lenci, arXiv:2112.14248, give the same forbidden-word generating-function framework and maximizer classification but not the second-moment or allocation law. Bunimovich–Yurchenko, arXiv:0811.4438, concerns positional period ordering; Dettmann, arXiv:1112.5390, concerns fixed-position small-hole asymptotics. McGoff, arXiv:1809.05586, samples a different ensemble of many independently selected forbidden words. Comparable mathematical results indexed under pair correlations or moving-hole escape do not imply the claim. Search and source inspection did not locate an exact equivalent, but absence of an indexed or accessible proof cannot exclude historical priority. The known mean and spectral formulas are credited explicitly.

## Mathematical value — PASS

Randomly selecting one Markov hole is a natural ensemble in open chaotic dynamics. Its mean normalized escape rate approaches one, masking unusually slow leakage near short cycles. The sharp \(q^{-n}\) variance and explicit \(K_q\) quantify the remaining heterogeneity; the full variance-weighted least-period distribution identifies **which** exceptional holes account for that heterogeneity and establishes that the limiting allocation has total mass one. These are nontrivial exact dynamical-statistical invariants over an infinite family, not a relabeling of individual-hole escape rates or a known-table recomputation. No conjecture of universality beyond this model is made.

## Scope and outstanding limitations

The statement is for one fixed cylinder hole, uniform selection among \(q^n\) sites, Lebesgue initial data, fixed integer \(q\), and \(n\to\infty\). It does not cover moving leaks, arbitrary interval shapes or distorted maps. Full independent historical or mathematical review has not been done, and an unindexed calculation derived from the known periodic-orbit machinery may exist.

Self-review: passed. Independent audit: not yet performed.
