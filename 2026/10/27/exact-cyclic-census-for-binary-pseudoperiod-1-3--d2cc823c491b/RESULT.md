# Exact cyclic census for binary pseudoperiod \((1,3)\)

## Finding
For every positive integer \(n\), let \(\mathcal P_n\) be the set of indexed binary words \(w=w_0\cdots w_{n-1}\) whose periodic extension satisfies
\[
  w_i\in\{w_{i+1},w_{i+3}\}\qquad(i\in\mathbb Z),
\]
with indices interpreted modulo \(n\). Let \(C_{n,t}\) count members of \(\mathcal P_n\) with exactly \(t\) cyclic unequal-adjacency transitions. Then the **complete transition-refined enumeration** is
\[
 C_{n,t}=\begin{cases}
 2,&t=0,\\[2pt]
 \displaystyle\frac{2n}{n-t}\binom{n-t}{2t-n},
   &t\ge2\text{ even},\quad n\le2t,\quad3t\le2n,\\[5pt]
 0,&\text{otherwise}.
 \end{cases}
\]
Every nonconstant member is characterized by its cyclic transition word: the latter has an even number of ones and is a cyclic concatenation of the two blocks `10` and `110`.

Writing \(A_n=\sum_t C_{n,t}\), the bivariate generating function and dynamical zeta function are, respectively,
\[
 \mathcal C(z,u)=\sum_{n\ge1}\sum_{t\ge0}C_{n,t}z^nu^t
 =\frac{2z}{1-z}
 +\frac{2uz^2+3u^2z^3}{1-uz^2-u^2z^3}
 +\frac{-2uz^2+3u^2z^3}{1+uz^2-u^2z^3},
\]
\[
 \zeta(z):=\exp\!\left(\sum_{n\ge1}\frac{A_n}{n}z^n\right)
 =\frac{1}{(1-z)^2\big((1-z^3)^2-z^4\big)}.
\]
The first twenty values of \(A_n\), beginning at \(n=1\), are
\[
2,2,8,6,2,8,16,6,8,32,24,12,54,72,38,86,172,134,154,356.
\]
The exact number of primitive rotation classes of circumference \(n\) is
\[
 P_n=\frac1n\sum_{d\mid n}\mu(d)A_{n/d},
\]
where \(\mu\) is the ordinary number-theoretic Möbius function. If \(\lambda\) is the unique positive root of \(\lambda^3-\lambda-1=0\), then
\[
 A_n=\lambda^n+O(1.22^n),\qquad
 P_n\sim\frac{\lambda^n}{n},\qquad
 h_{\mathrm{top}}=\log\lambda.
\]
Here \(h_{\mathrm{top}}\) is the topological entropy of the two-sided binary shift defined by the displayed pseudoperiod condition, and \(\lambda\approx1.324717957\) is the plastic constant.

## Assumptions and scope
Words are indexed, not identified under rotation unless explicitly stated. A period-\(n\) word need not have *least* period \(n\); \(P_n\) counts only rotation classes of least period \(n\). The two constant words are present for each \(n\ge1\). A cyclic transition is an index \(i\) with \(w_i\ne w_{i+1}\). The periodic-extension definition is stronger than merely testing the finite-word pseudoperiod condition at positions with all shifted positions remaining inside the given finite word. All counts include circumference \(n=1\) and \(n=2\).

## Proof
**1. Transition characterization.** Set \(d_i=w_i\oplus w_{i+1}\in\{0,1\}\), with indices cyclic and \(\oplus\) denoting addition modulo two. The equality \(w_i=w_{i+3}\) is equivalent to \(d_i\oplus d_{i+1}\oplus d_{i+2}=0\). Consequently the pseudoperiod condition holds exactly when every cyclic triple beginning with a \(1\) in \(d\) is `101` or `110`: the forbidden triples are exactly `100` and `111`. A cyclic difference vector comes from a binary cyclic word if and only if \(\sum_i d_i\equiv0\pmod2\), in which case the initial bit may be chosen freely, yielding exactly two lifts.

If \(d\) is nonzero and avoids `111`, at least one zero occurs. The forbidden triple `100` forces every cyclic zero-run to have length exactly one, while forbidden `111` forces every one-run to have length one or two. Thus nonzero valid transition vectors are *precisely* cyclic concatenations of `10` and `110`, with the additional even-number-of-ones lifting condition. The all-zero vector gives the two constants. This reasoning also holds for small circumferences because cyclic triples use repeated indices when necessary.

**2. Exact counting.** Suppose a nonzero cyclic transition word contains \(r\) blocks `10` and \(s\) blocks `110`. Its length, transition count, and number of cyclic zeros are
\[
 n=2r+3s,\qquad t=r+2s,\qquad k=r+s=n-t.
\]
Hence \(s=2t-n\) and \(r=2n-3t\). Nonnegative integers \(r,s\) are possible exactly when \(n\le2t\) and \(3t\le2n\); the lift additionally requires even \(t\). To count indexed transition words, mark one of the \(k\) zeros, choose its position among \(n\) indexed coordinates, and prescribe the ensuing cyclic sequence of \(k\) block lengths, of which \(s\) are three. There are \(n\binom{k}{s}\) such marked objects, while each indexed transition word admits exactly \(k\) marks. Thus the number of indexed transition words is \(n\binom{k}{s}/k\). Multiplying by the two choices of initial bit gives the formula for \(C_{n,t}\).

**3. Generating function and zeta function.** Use the four states `00`, `01`, `10`, `11` for consecutive pairs of transition bits. From state \((a,b)\) to \((b,c)\), allow an edge if \(a=0\) or \(b\ne c\), weighted \(u^a\). The transfer matrix is
\[
 T(u)=\begin{pmatrix}
 1&1&0&0\\
 0&0&1&1\\
 0&u&0&0\\
 0&0&u&0
 \end{pmatrix},
 \qquad
 \det(I-zT(u))=(1-z)(1-uz^2-u^2z^3).
\]
Closed walks of length \(n\) correspond bijectively to indexed cyclic transition vectors satisfying the local constraint. The even-parity projection, together with the two binary lifts, therefore gives
\[
 \sum_t C_{n,t}u^t=\operatorname{tr}(T(u)^n)+\operatorname{tr}(T(-u)^n).
\]
For any finite matrix \(T\), the formal identity \(\sum_{n\ge1}\operatorname{tr}(T^n)z^n=-z\,\partial_z\log\det(I-zT)\) follows by expanding the logarithm. Applying it to both matrices yields the stated explicit rational \(\mathcal C(z,u)\). Setting \(u=1\), integrating the log-derivative coefficientwise, and imposing constant term one yields the stated \(\zeta(z)\).

**4. Primitive classes and growth.** A repetition of any admissible cyclic word remains admissible. If \(Q_n\) counts admissible indexed words of least period \(n\), then \(A_n=\sum_{d\mid n}Q_d\). Möbius inversion gives \(Q_n=\sum_{d\mid n}\mu(d)A_{n/d}\), and each primitive rotation class has exactly \(n\) indexed representatives, so \(P_n=Q_n/n\).

The eigenvalues of \(T(1)\) comprise \(1\) and the three roots of \(x^3-x-1\); those of \(T(-1)\) comprise \(1\) and the roots of \(x^3+x-1\). The former cubic has one dominant real root \(\lambda>1\), and all other eigenvalues of these two matrices have modulus less than \(1.22\). The trace formula proves \(A_n=\lambda^n+O(1.22^n)\); Möbius inversion proves \(P_n\sim\lambda^n/n\). The difference-coordinate map is a two-to-one factor map from the pseudoperiodic shift to the triple-avoidance shift, so these finite-to-one shifts have the same topological entropy. The latter is the spectral-radius entropy \(\log\lambda\) of its four-state finite-type presentation.

## Verification
The standalone `verify.py` exhaustively evaluates all \(524{,}286\) binary words of lengths \(1\) through \(18\) against the original shift condition and compares each transition count with the binomial formula. It separately computes transition vectors, their forbidden triples, and the count through length \(14\). A direct four-state polynomial transfer-matrix computation agrees through length \(70\); a distinct Newton-sum recurrence for the two cubic factors agrees through length \(180\). These finite checks support but do not replace the all-length argument above. Execute using `python3 verify.py` from the package directory; no external dependencies are required.

## Relationship to prior work
Meleshko, Ochem, Shallit, and Shan introduced and studied the pseudoperiod condition, including the rigid \((1,2)\) classification and critical-exponent questions for \((1,3)\). Their published article does not state a circular transition-refined count, a primitive-cycle census, or this specific zeta function. The present result studies periodic points of a specified pseudoperiod class rather than constructing low-critical-exponent infinite words. Boyle and Schmieding discuss general group extensions of shifts of finite type and the standard determinant expression for periodic data. That general framework explains why a transfer expression is available, but it does not identify the `10`/`110` constrained renewal structure or its exact even-parity binomial coefficients for this pseudoperiod. General finite-state computability and determinant methods are not claimed as new.

## Limitations
The result applies to binary alphabet, the single specified pseudoperiod \((1,3)\), and periodic-extension/circular counts. It does not classify nonperiodic sequences by critical exponent or solve the unrestricted pseudoperiod problem. The underlying finite-state transfer and renewal-counting techniques are standard; the instance-specific structural reduction and all-circumference refined formula are the proposed contribution. Mathematical novelty relative to a potentially unlocated equivalent necklace or renewal-system enumeration remains subject to independent literature review. No independent audit has been carried out.

## References
1. J. Meleshko, P. Ochem, J. Shallit, S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, first public arXiv version July 20, 2022, arXiv:2207.10171; *Discrete Mathematics & Theoretical Computer Science* 25:2 (2023), article 9919. https://arxiv.org/abs/2207.10171
2. M. Boyle and S. Schmieding, *Finite Group Extensions of Shifts of Finite Type: K-theory, Parry and Livšic*, arXiv:1503.02050, *Ergodic Theory and Dynamical Systems* 37 (2017), 1026–1059. https://arxiv.org/abs/1503.02050
