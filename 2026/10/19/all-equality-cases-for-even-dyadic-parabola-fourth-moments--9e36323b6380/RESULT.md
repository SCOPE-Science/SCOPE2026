# All equality cases for even dyadic parabola fourth moments

## Finding
For every integer \(k\ge1\), set \(N=2^{2k}\), \(R=\mathbb Z/N\mathbb Z\), and
\[
\mathcal E_k f(u,v)=\frac1N\sum_{t\in R}f(t)\exp\!\left(\frac{2\pi i(ut+vt^2)}N\right).
\]
The sharp fourth-moment inequality, with counting output and normalized input, is
\[
\sum_{u,v\in R}|\mathcal E_k f(u,v)|^4
\le 3\,2^{k-1}\left(\frac1N\sum_{t\in R}|f(t)|^2\right)^2.
\]
**Complete equality classification.** A nonzero complex function \(f\) attains equality **if and only if** there exist uniquely determined integers \(0\le r<2^{k-1}\) and \(0\le j<2^k\), a nonzero scalar \(c\in\mathbb C\), and a circle parameter \(\omega\in\mathbb C\) with \(|\omega|=1\), such that \(f\) vanishes outside the coset \(r+2^{k-1}R\) and
\[
\boxed{f(r+2^{k-1}\eta+2^k u)
=c\,\omega^\eta\exp(2\pi i j u/2^k),
\quad \eta\in\{0,1\},\quad u\in\mathbb Z/2^k\mathbb Z.}
\]
The displayed parameterization uses the unique representatives \(r\in\{0,\ldots,2^{k-1}-1\}\). The two daughter cosets have equal nonzero magnitude and one shared additive-character frequency, but their relative phase is entirely free. Modulo nonzero global complex scaling, the optimizer space is a disjoint union of precisely \(2^{2k-1}\) circles.

## Assumptions and scope
All calculations take place in the cyclic ring \(R=\mathbb Z/2^{2k}\mathbb Z\). Every complex input, including functions with zeros, is allowed. Fourier output uses counting measure on \(R^2\); the input squared norm is normalized by \(N^{-1}\). Equality is only asserted for nonzero inputs. The result classifies maximizers for every **even** dyadic exponent; it does not assert any classification for odd exponents, non-dyadic rings, or higher moments. The sharp numerical constant was previously established; the theorem here supplies the missing necessity and sufficiency of its complete complex equality family.

## Proof
Write \(S=\sum_{t\in R}|f(t)|^2\), and define the exact quartic incidence form
\[
Q(f)=\sum_{\substack{a+b=c+d\\a^2+b^2=c^2+d^2}}
 f(a)f(b)\overline{f(c)f(d)},
\]
with both congruences taken modulo \(N\). Orthogonality of all additive characters of \(R^2\) gives
\[
\sum_{u,v\in R}|\mathcal E_k f(u,v)|^4=N^{-2}Q(f).
\tag{1}
\]

**Autocorrelation and the sharp energy majorant.** For each \(h\in R\), let \(K_h=\{z\in R:2hz=0\}\). Substituting \((a,b,c,d)=(x+h,y,x,y+h)\) in the defining congruences, one obtains the nonnegative identity
\[
Q(f)=\sum_{h\in R}\sum_{A\in R/K_h}
\left|\sum_{x\in A}f(x+h)\overline{f(x)}\right|^2.
\tag{2}
\]
Cauchy--Schwarz within every coset, then rearrangement, yields
\[
Q(f)\le\sum_{x,y\in R}|f(x)|^2|f(y)|^2M(x-y),
\quad M(d)=\#\{h\in R:2h(d-h)=0\}.
\tag{3}
\]
Let \(\nu_2(d)\) be the truncated valuation, with \(\nu_2(0)=2k\). Elementary congruence counting gives, **for every** \(d\in R\),
\[
M(d)=\begin{cases}
2^{r+2},&r=\nu_2(d)<k,\\
2^k,&r\ge k.
\end{cases}
\tag{4}
\]
To prove (4), note that \(2h(d-h)=0\) is the same as \(h(d-h)=0\) modulo \(2^{2k-1}\). If \(r<k\), the two disjoint solution families are \(h\equiv0\) and \(h\equiv d\pmod {2^{2k-1-r}}\); each has \(2^{r+1}\) members modulo \(N\). If \(r\ge k\), precisely the multiples of \(2^k\) solve the congruence, giving \(2^k\) members. The arguments also cover \(k=1\) and \(d=0\).

Put \(L=2^kR\) and \(H=2^{k-1}R\). Formula (4) implies
\[
M(d)\le 2^k\bigl(1+\mathbf1_{H\setminus L}(d)\bigr),
\tag{5}
\]
with equality whenever \(d\in H\). Partition the mass \(|f|^2\) among the cosets of \(H\) and their two constituent \(L\)-cosets. For parent coset \(A\), denote the daughter masses by \(X_A,Y_A\). Then
\[
\sum_{x,y}|f(x)|^2|f(y)|^2\mathbf1_{H\setminus L}(x-y)
=2\sum_A X_A Y_A\le\frac12\sum_A(X_A+Y_A)^2\le\frac12S^2.
\tag{6}
\]
Thus \(Q(f)\le3\,2^{k-1}S^2\), equivalent by (1) to the stated inequality. For nonzero \(f\), equality in (6) is possible **only** if all mass lies in one parent coset \(r+H\) and the two daughter masses are equal and positive. These conditions are necessary for any extremizer; because (5) is an equality on \(H\), no strict loss remains in the collision-weight estimate for such a support.

**Cauchy equality forces one common character.** If equality holds in the sharp inequality, every term in the nonnegative Cauchy defect in (2)--(3) vanishes. Choose the single translation \(h=2^k\), which generates the cyclic subgroup \(L\). Directly from its definition, \(K_h=H\). Since all mass is in \(r+H\), equality in the Cauchy--Schwarz inequality on this particular \(K_h\)-coset forces
\[
f(x+2^k)=\lambda f(x)\qquad(x\in r+H),
\tag{7}
\]
for a fixed complex \(\lambda\). Translation by \(2^k\) permutes the parent coset, so \(|\lambda|=1\); iterating its order \(2^k\) and using nonzero mass gives \(\lambda^{2^k}=1\). Write \(\lambda=\exp(2\pi i j/2^k)\). Each daughter is a single orbit of that translation, so (7) gives a constant magnitude and the same \(j\) in both daughters. Equality of daughter masses forces their base magnitudes to match, leaving precisely one arbitrary unit relative phase \(\omega\). This proves **necessity** and uniqueness of \(r,j\) and of \(\omega\) after fixing the displayed base point and overall scale.

**Every displayed packet is an extremizer.** Let \(f\) have the specified form. For \(h\in L\), shifting by \(h\) multiplies \(f\) by one scalar on all of \(r+H\), so Cauchy--Schwarz is an equality in (2) for these \(h\). For \(h\in H\setminus L\), the subgroup \(K_h\) equals \(L\); shifting by \(h\) swaps the daughters and gives a constant multiplicative factor separately on each daughter, so Cauchy--Schwarz is again an equality. No \(h\notin H\) contributes a nonzero correlation term, since the support and its translate are disjoint. Consequently (2)--(3) is an equality. Moreover, every difference of two support points belongs to \(H\), where (5) is exact; the two equal daughter masses make (6) exact. Hence \(Q(f)=3\,2^{k-1}S^2\), proving sufficiency.

Finally, distinct cosets \(r+H\) have disjoint support; within one coset, distinct values of \(j\) yield distinct translation eigenvalues. After quotienting by a nonzero scalar, the remaining parameter \(\omega\) runs once around a unit circle. Thus there are exactly \(2^{k-1}\cdot2^k=2^{2k-1}\) circle components.

## Verification
The included `checker.py` enumerates the exact congruence counts \(M(d)\) for all differences in cyclic rings of orders \(4\), \(16\), \(64\), and \(256\). Independently it computes the fourth moment by collecting all exact finite-group two-sum fibers, then evaluates complex packet families with several phases and all listed coset choices. It verifies the sharp ratio and supplies a strict nonextremal daughter-only witness at each tested order. The actual replay output is included as `checker_output.txt`. Floating complex computations are checked within a stated tolerance; the all-order theorem rests on the preceding exact arithmetic and equality proof, not on finite experiments.

## Relationship to prior work
Hickman and Wright (2018) study Fourier restriction for polynomial graphs on residue rings; their general restriction estimates do not classify complex equality cases for the even dyadic parabola fourth moment. González-Riquelme and Oliveira e Silva (2024) prove sharp Fourier extension inequalities on finite fields; that setting has no nilpotent dyadic layers. The earlier exact dyadic result *Parity-sharp fourth moments of the dyadic quadratic graph* (public mathematical record 417e488b0292, 2026) establishes the sharp constant \(3\,2^{k-1}\) and coset-indicator examples, but explicitly does **not** characterize all maximizers. The present theorem supplies the **complete complex equality classification**, including discrete character frequencies and continuous daughter-phase circles. A related published classification for **odd** prime-power parabolas does not imply the dyadic statement: its congruence-count structure and even-exponent constants differ.

## Limitations
The sharp constant and its existing proof are prior results; the new mathematical assertion is the if-and-only-if equality classification and the exact topology/count of the projective extremizer set. No statement is made about sharp higher Fourier moments, odd dyadic exponents, or composite moduli with odd factors. Potential equivalent classifications expressed through positive-definite kernels, convolution incidence, or local representation theory remain a bibliographic originality risk. The numerical verifier samples finitely many moduli and phases and is not an independent proof of the quantified theorem.

## References
1. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176v1, first posted 2018-01-09; *Discrete Analysis* 2018:11. https://arxiv.org/abs/1801.03176
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first posted 2024-05-26. https://arxiv.org/abs/2405.16647
3. *Parity-sharp fourth moments of the dyadic quadratic graph*, public mathematical record 417e488b0292 (2026), especially its Finding, Proof and Limitations sections.
4. *Exact fourth-moment extension and all extremizers for parabolas over odd prime-power rings*, public mathematical record 730a12e98b61 (2026). The prime-two case is excluded by its hypotheses.
