# Exact subsequence-universality law under a bounded zero-run constraint

## Finding
Fix an integer \(r\ge 1\), the binary alphabet \(\Sigma=\{0,1\}\), and the language \(\mathcal L_r\) of finite words having no factor \(0^{r+1}\). For a word \(w\), define its *subsequence-universality index* \(\iota(w)\) as the largest integer \(k\ge 0\) for which every binary word of length \(k\) occurs as a scattered subsequence of \(w\). Define
\[
N_{r,n,k}=|\{w\in\mathcal L_r\cap\Sigma^n:\iota(w)=k\}|.
\]
For all \(r\ge 1\), simultaneously for every \(n,k\ge0\), the complete bivariate distribution is
\[
\boxed{F_r(z,u)=\sum_{n,k\ge0}N_{r,n,k}z^nu^k
=\frac{1+z-z^{r+1}-uz^{r+2}}{1-z-2uz^2+uz^{r+2}+u^2z^{r+3}}.}
\]
In particular, setting \(u=1\) gives the exact unweighted count
\[
F_r(z,1)=\frac{1+z+\cdots+z^r}{1-z-z^2-\cdots-z^{r+1}}.
\]

Let \(W_{r,n}\) be uniformly distributed among the words of \(\mathcal L_r\cap\Sigma^n\). Let \(\rho_r\) be the unique positive solution of \(\rho_r+\rho_r^2+\cdots+\rho_r^{r+1}=1\). Then
\[
\mathbb E[\iota(W_{r,n})]=\mu_r n+O_r(1),\qquad
\mu_r=\left.\frac{\partial_uD_r(z,u)}{z\,\partial_zD_r(z,u)}\right|_{z=\rho_r,u=1},
\]
where \(D_r(z,u)=1-z-2uz^2+uz^{r+2}+u^2z^{r+3}\). The efficiency comparison is **sharp at the smallest two run limits**:
\[
\boxed{\mu_1=\frac12-\frac{\sqrt5}{10}<\frac13<\mu_r\quad(r\ge2),\qquad \lim_{r\to\infty}\mu_r=\frac13.}
\]
The reference value \(1/3\) is the asymptotic universality-index rate of an unrestricted uniformly random binary word. Thus forbidding \(00\) lowers the rate, whereas forbidding a sufficiently long all-zero run with limit \(r\ge2\) increases it.

## Assumptions and scope
The alphabet is fixed as \(\{0,1\}\), including for unary and empty words; the empty word has index zero. Occurrences are **scattered** subsequences, not contiguous factors. A zero-run constraint forbids \(r+1\) consecutive zeros but places no limit on runs of ones. The index counts complete greedy arches; the incomplete final tail counts zero additional arches. The distribution counts labeled linear words, not cyclic classes, and uses ordinary—not exponential—generating functions.

## Proof
**1. Exact interpretation of the index.** Greedily cut the shortest next prefix containing both binary letters, and repeat until the remaining suffix has only one letter or is empty. Every completed block (arch) contains both letters, so an arbitrary length-\(k\) binary word embeds by choosing its \(i\)-th letter from the \(i\)-th arch whenever at least \(k\) arches exist. Conversely, let the completed arches end with letters \(c_1,\ldots,c_h\). Each \(c_i\) appears for the first time within its own arch at its last position. Therefore the greedy earliest embedding of \(c_1\cdots c_h\) ends at the end of the \(h\)-th arch. Append a letter absent from the incomplete rest: the resulting length-\(h+1\) word cannot be a subsequence. Consequently \(\iota(w)=h\).

**2. Finite-state suffix equations.** Weight each appended letter by \(z\) and each completed arch by \(u\). After the last completed arch, let \(E_1\) be the generating function for allowable continuations when its last symbol was \(1\), and let \(E_0\) be the corresponding function when it was \(0\). In either case the arch mask resets to empty. Let \(B\) be the continuation series when the current incomplete arch has seen only \(1\); let \(A_j\) be the continuation series when it has seen only \(0\) and the suffix currently ends with exactly \(j\) consecutive zeros. The allowed values are \(1\le j\le r\). Each series includes the empty continuation.

After an arch ending in \(1\), the restriction carries no pending zero-run; therefore \(E_1=F_r\), the same series as a fresh start. The recurrences are
\[
A_j=1+zuF_r+zA_{j+1}\quad(1\le j<r),\qquad A_r=1+zuF_r,
\]
\[
B=1+zB+zuE_0,\qquad
E_0=1+zB+zA_2,\qquad F_r=1+zB+zA_1.
\]
Here set \(A_2=0\) when \(r=1\). The two terms in \(B\) correspond to appending another \(1\) or a completing \(0\). The transition from an incomplete all-zero arch to a \(1\) completes it and returns to \(E_1=F_r\).

With \(S_m(z)=1+\cdots+z^{m-1}\) for \(m\ge1\), and \(S_0=0\), the first recurrence gives \(A_1=S_r(z)(1+zuF_r)\) and \(A_2=S_{r-1}(z)(1+zuF_r)\). Subtract the equations for \(E_0\) and \(F_r\) to obtain
\[
E_0=F_r-z^r(1+zuF_r).
\]
Substitute this and \(B=(1+zuE_0)/(1-z)\) into the formula for \(F_r\). Since \((1-z)S_r(z)=1-z^r\), clearing the denominator gives the exact identity
\[
(1-z-2uz^2+uz^{r+2}+u^2z^{r+3})F_r
=1+z-z^{r+1}-uz^{r+2}.
\]
Its denominator has constant term one, so it determines all coefficients uniquely as formal power series, proving the boxed formula for all \(r,n,k\).

**3. Ordinary counts and the asymptotic slope.** At \(u=1\), both the numerator and denominator have the factor \(1-z^2\), leaving the displayed unweighted rational series. Write \(T_r(z)=1-\sum_{j=1}^{r+1}z^j\). The positive real zero \(\rho_r\in(1/2,1)\) is simple because \(T'_r(\rho_r)<0\); it has strictly smaller modulus than any other zero since all lengths of admissible runs occur in the recurrence (the corresponding finite-state graph is primitive). The nonzero residue of \(F_r(z,1)\) at \(\rho_r\) therefore controls the asymptotics. Near \(u=1\) the same unique dominant zero \(\rho_r(u)\) of \(D_r(z,u)\) is analytic; coefficient ratios imply
\[
\mathbb E[\iota(W_{r,n})]=-n\,\frac{\rho'_r(1)}{\rho_r(1)}+O_r(1).
\]
Implicit differentiation of \(D_r(\rho_r(u),u)=0\) yields the formula for \(\mu_r\).

**4. Strict efficiency reversal.** At \(z=\rho_r\), the denominator derivative is \(\partial_zD_r(z,1)=(1-z^2)T'_r(z)<0\). Direct algebra gives
\[
3\,\partial_uD_r(z,1)-z\,\partial_zD_r(z,1)
=z(1-2z)+(1-r)z^{r+2}+(3-r)z^{r+3}.
\]
For \(r\ge3\) this is strictly negative because \(\rho_r>1/2\). For \(r=2\) it becomes \(z(1-2z)-z^4(1-z)<0\). Dividing by \(3z\partial_zD_r<0\) shows \(\mu_r>1/3\). For \(r=1\), the positive root is \((\sqrt5-1)/2\) and direct substitution gives \(\mu_1=1/2-\sqrt5/10<1/3\). Finally \(\rho_r\to1/2\) as \(r\to\infty\), and all correction terms in the derivative formula vanish; hence \(\mu_r\to1/3\). The unrestricted limit also follows directly by taking the coefficientwise limit \(F_r(z,u)\to(1+z)/(1-z-2uz^2)\).

## Verification
The standalone file `verify.py` computes the index from the greedy definition, independently checks it against the defining all-subsequences test for all binary words of length at most \(10\), and compares three routes to the same histogram: direct word enumeration for all \(r\in\{1,\ldots,8\}\) and \(0\le n\le14\), a run-limit/arch-mask transition-counting automaton for \(0\le n\le125\), and the recurrence obtained by coefficient extraction from the claimed rational identity for the same ranges. An independent recurrence for ordinary zero-run-limited word counts checks the specialization \(u=1\). The code also verifies reduction to the unrestricted length counts when the forbidden zero-run exceeds the word length.

Run `python3 verify.py`. A successful replay prints `RUN_LIMIT_ARCH_LAW_PASS`. These finite computations corroborate, but do not replace, the all-parameter formal-series proof above. The numerical value \(\mu_2\approx0.358904097337774\) is obtained by substituting the unique positive root of \(z+z^2+z^3=1\) into the exact derivative expression.

## Relationship to prior work
Barker and collaborators established the fundamental arch-factorization and scattered-factor universality framework. Adamson obtained efficient counting/ranking algorithms for unrestricted \(k\)-subsequence-universal words and explicitly raised the issue of closed formulas. Adamson, Fleischmann, Huch, Koß, Manea, and Nowotka gave more general algorithms for counting \(k\)-universal words accepted by finite automata. That result covers the *computational possibility* of recovering any fixed coefficient for each regular language, but does not state this uniform-in-\(r\) rational distribution or the strict sign change in its limiting rate. A previously published binary unconstrained distribution equals the coefficientwise \(r\to\infty\) specialization \((1+z)/(1-z-2uz^2)\); it is acknowledged and not claimed as new. Classical run-length-constrained enumeration records the unweighted \(u=1\) part, not the arch-refined formula or efficiency comparison.

## Limitations
The constraint is asymmetric (only zero-runs are bounded). The result does not supply analogous simplified rational formulas for simultaneous independent bounds on both symbols or for alphabets larger than two. The moment estimate concerns fixed \(r\) followed by \(n\to\infty\), not a joint limit with \(r\) varying with \(n\). Searching did not establish universal novelty across every unpublished manuscript, and the general regular-language counting algorithms remain a potential route by which an equivalent expression could be independently derived. No independent mathematical audit is claimed.

## References
1. Laura Barker, Pamela Fleischmann, Katharina Harwardt, Florin Manea, Dirk Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, 2020-03-10. https://arxiv.org/abs/2003.04629
2. Duncan Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1, 2023-04-10. https://arxiv.org/abs/2304.04583
3. Duncan Adamson, Pamela Fleischmann, Annika Huch, Tore Koß, Florin Manea, Dirk Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1, 2023-11-17. https://arxiv.org/abs/2311.10658
4. Oleg Kurmaev, *Constant-Weight and Constant-Charge Binary Run-Length Limited Codes*, arXiv:0902.4246v1, 2009-02-24. https://arxiv.org/abs/0902.4246
5. *Closed-form law for binary subsequence universality*, public mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37
