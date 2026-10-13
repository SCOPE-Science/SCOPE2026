# Review of a prime-support theorem

## Correctness — PASS
The precise theorem covers all composite positive integers and exactly excludes the exceptional solution \(4\). The proof first ensures the integer quotient \(K=(n-1)/\beta(n)\ge2\). For even integers, the parity of each odd-prime local factor forces even exponents and two rational lower bounds contradict the only possible odd quotient \(K=3\). For odd integers, separate prime-support inequalities reduce the problem to \(3^a5^br^c\) with \(r\in\{7,11,13\}\) and \(K=2\); exact power bounds and congruences modulo \(4\), \(3\), and \(5\) exclude these. All ranges of exponents are covered. Reproduction is provided by `verify.py` and is explicitly not substituted for proof.

## Originality — PASS with residual risk
Tóth (arXiv:1111.4842; 2011) formulates precisely \(\beta(n)\mid n-1\) as an open composite-number question and reports a finite computation, not these parity-differentiated unrestricted prime-support bounds. Iannucci (2006) studies the equivalent arithmetic function under another symbol, but for the different relation \(k\beta(n)=n\). The classical Lehmer problem in \(\varphi\) agrees only on squarefree inputs. Published and sequence searches for the exact divisibility, aliases, and lower-support cases did not reveal a covering result. A public but unindexed elementary proof remains a risk; the search is not a uniqueness certificate.

## Value — PASS
The question is explicitly posed in the primary literature, and the result rules out all three-prime-support composites and all even four-prime-support composites **regardless of exponents**. The even case uses an additional parity-to-quotient obstruction; the odd case isolates and destroys a small, natural exceptional support set. These are structural exclusions over unbounded families, not a numerical table or a conditional construction. No stronger existence claim or paper-sized result is asserted.

Self-review: passed. Independent audit: not yet performed.
