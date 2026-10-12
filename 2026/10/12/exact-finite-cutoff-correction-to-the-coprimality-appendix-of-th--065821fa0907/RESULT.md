# Exact finite-cutoff correction to the coprimality appendix of the continuous-variable Shor algorithm

## Finding
The finite-cutoff coprimality bounds printed in the number-theoretic appendix of *A Continuous Variable Shor Algorithm* are not valid for every cutoff \(N\ge a\). Define
\[
C_a(N)=\#\{1\le n\le N:\gcd(a,n)=1\}.
\]
Then Möbius inversion gives the exact count
\[
C_a(N)=\sum_{d\mid a}\mu(d)\left\lfloor\frac{N}{d}\right\rfloor.
\]
For \(a=6\) and \(N=10\), one has \(C_6(10)=3\), so
\[
\frac{C_6(10)}{10}=\frac3{10}<\frac13=\frac{\varphi(6)}6.
\]
This disproves the appendix's Proposition 2 as a finite-uniform statement.

Let \(J_a(N)\) count ordered pairs \((n_1,n_2)\) with \(1\le n_1,n_2\le N\) and
\[
\gcd(a,n_1)=\gcd(a,n_2)=\gcd(n_1,n_2)=1.
\]
A second Möbius inversion gives
\[
J_a(N)=\sum_{\substack{1\le d\le N\\(d,a)=1}}\mu(d)\,C_a\!\left(\left\lfloor\frac Nd\right\rfloor\right)^2.
\]
Therefore the conditional probability appearing in Proposition 3 is exactly \(J_a(N)/C_a(N)^2\), while the joint probability used in Corollary 2 is exactly \(J_a(N)/N^2\). At \(a=3,N=4\), \(C_3(4)=3\) and \(J_3(4)=5\), so
\[
\frac{J_3(4)}{C_3(4)^2}=\frac59<\frac6{\pi^2}.
\]
At \(a=5,N=6\), \(J_5(6)=13\), hence
\[
\frac{J_5(6)}{36}=\frac{13}{36}<\frac{96}{25\pi^2},
\]
so Corollary 2 also fails as a finite-uniform lower bound.

For every fixed \(a\), the intended asymptotic mechanism survives. Periodicity gives \(C_a(M)/M\to\varphi(a)/a\). Dominated convergence applied to the exact formula for \(J_a(N)\) yields
\[
\lim_{N\to\infty}\frac{J_a(N)}{N^2}
=\left(\frac{\varphi(a)}a\right)^2
\prod_{p\nmid a}(1-p^{-2})
=\left(\frac{\varphi(a)}a\right)^2
\frac{6/\pi^2}{\prod_{p\mid a}(1-p^{-2})}.
\]
Thus the finite statements require correction, while the familiar \(\Omega((\log\log a)^{-2})\) scale is recovered only after taking a sufficiently large cutoff for each fixed \(a\), rather than uniformly for all \(N\ge a\).

## Assumptions and scope
The claim concerns only the finite uniform integer model stated in the source's number-theoretic appendix. It does not assert that the continuous-variable quantum measurement itself produces an exactly uniform finite sample, and it does not claim that the overall quantum algorithm or its asymptotic motivation is invalid. The asymptotic statement is an iterated one: first \(N\to\infty\) with \(a\) fixed, then one may examine growth in \(a\).

## Proof
For the first formula use
\[
\mathbf 1_{\gcd(a,n)=1}=\sum_{\substack{d\mid a\\d\mid n}}\mu(d)
\]
and sum over \(1\le n\le N\). The counterexample \((a,N)=(6,10)\) is then exact.

For the pair count, use
\[
\mathbf 1_{\gcd(n_1,n_2)=1}=\sum_{d\mid n_1,\,d\mid n_2}\mu(d).
\]
Any common divisor \(d\) contributing to a pair already coprime to \(a\) must satisfy \((d,a)=1\). Writing \(n_i=dm_i\) leaves exactly \(C_a(\lfloor N/d\rfloor)\) choices for each \(m_i\), which proves the formula for \(J_a(N)\). Direct evaluation gives the two finite counterexamples above.

For fixed \(a\), periodicity of reduced residue classes gives \(C_a(M)/M\to\varphi(a)/a\). For each fixed \(d\) coprime to \(a\),
\[
\frac{C_a(\lfloor N/d\rfloor)^2}{N^2}\to \left(\frac{\varphi(a)}a\right)^2\frac1{d^2}.
\]
Moreover \(C_a(\lfloor N/d\rfloor)\le N/d\), so the summands are dominated by \(d^{-2}\). Dominated convergence therefore gives the series over \(\mu(d)/d^2\), and absolute convergence yields the Euler product over primes not dividing \(a\).

## Verification
The accompanying standard-library checker independently evaluates the exact Möbius formulas against brute-force counting for every \(2\le a\le30\) and \(1\le N\le60\), verifies all three explicit counterexamples, and numerically checks the fixed-\(a\) limiting density for several values of \(a\). Its successful terminal line is:

`VERIFY_OK exact_grid=29x60 prop2=3/10<1/3 prop3=5/9<6/pi^2 cor2=13/36<96/(25*pi^2)`

The finite exhaustive computation is not used as a proof of the infinite asymptotic statement; that statement is proved analytically above.

## Relationship to prior work
The anchor source states Proposition 2, Proposition 3, and Corollary 2 in its number-theoretic appendix and invokes the corollary in its rational-period repetition estimate. The final arXiv revision retains those statements. A later paper by the same authors on continuous hidden-subgroup algorithms discusses related continuous Fourier-sampling constructions but, in the inspected material, does not supply this finite-cutoff correction. A broad hidden-subgroup review provides context but does not imply the formulas above. Targeted searches for the source identifier, proposition wording, coprimality bound, and errata did not reveal an equivalent correction.

## Limitations
The result corrects only the stated finite probability lemmas and their use as a uniform finite-cutoff justification. It does not analyze physical noise, finite detector resolution, the precise distribution induced by a generalized quantum measurement, or total algorithmic complexity under a fully specified implementation. An unindexed erratum or differently worded note could still contain the same correction.

## References
1. S. J. Lomonaco Jr. and L. H. Kauffman, *A Continuous Variable Shor Algorithm*, arXiv:quant-ph/0210141; later published in *Quantum Information and Computation II*, Contemporary Mathematics 381, DOI 10.1090/conm/381/07093.
2. S. J. Lomonaco Jr. and L. H. Kauffman, *Continuous Quantum Hidden Subgroup Algorithms*, arXiv:quant-ph/0304084.
3. C. Lomont, *The Hidden Subgroup Problem — Review and Open Problems*, arXiv:quant-ph/0411037.
