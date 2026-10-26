# Exact finite-alphabet inverse-list spectrum for a two-symbol palindromic duplication

## Finding
Fix an integer \(q\ge 2\) and an alphabet \(\Sigma_q\) with \(q\) symbols. A length-two palindromic duplication replaces \(uabv\) by \(uabbav\), where \(u,v\) are arbitrary words. For every received word \(y\in\Sigma_q^N\), let \(L(y)\) be the number of **distinct** length-\(N-2\) parents under exactly one such operation; set \(L(y)=0\) when \(N<4\).

The complete population generating function is
\[
F_q(z,t)=\sum_{N\ge1}\sum_{y\in\Sigma_q^N}z^N t^{L(y)}
=\frac{q\bigl(z+(t-1)z^4\bigr)\bigl(1-(t-1)z^2\bigr)}{1-qz-(t-1)\bigl(z^2-z^3+(q-1)z^4\bigr)}.
\]
Thus, for every integer \(N\ge4\) and \(j\ge0\), the number of received words with exactly \(j\) parents is precisely \([z^Nt^j]F_q(z,t)\). This includes words with no parents. In particular, the complete quaternary length-eight population is \(47352,16924,1248,12\) for respective inverse-list sizes \(0,1,2,3\).

For a uniformly chosen receiver \(Y_N\in\Sigma_q^N\), the exact mean, for \(N\ge4\), is
\[
\mathbb E L(Y_N)=\frac{(q^2-1)N-3q^2+4}{q^4}.
\]
Define
\[
\mu_q=\frac{q^2-1}{q^4},\qquad
\nu_q=\frac{(q^2-1)(q^4-3q^2-2q+7)}{q^8}>0.
\]
Then, with \(q\) fixed as \(N\to\infty\),
\[
\operatorname{Var}(L(Y_N))=\nu_q N+O_q(1),\qquad
\frac{L(Y_N)-\mu_q N}{\sqrt{\nu_q N}}\Longrightarrow\mathcal N(0,1).
\]
The generating function and fluctuation law also hold for exact-one reverse-complement duplications of length two for any involutive complement on \(\Sigma_q\), via the even-length coordinate conjugacy of the cited 2026 work. The binary case \(q=2\), the worst-case inverse-list bound, and the aggregate first moment have predecessors; the distinguishing census result here is the full nonbinary spectrum and its fluctuation law.

## Assumptions and scope
All words have fixed length and are distinguished by their symbols and positions. A forward duplication inserts the reversed two-symbol source block immediately after that block. An inverse step searches for an occurrence \(abba\), deletes its last two symbols, and retains the first \(ab\). Identical parents produced from different inverse windows count once. The uniform law on \(\Sigma_q^N\) is over **all** potential received words, including unattainable ones, not over outputs sampled by first choosing a uniformly random source. No finite-field operations are assumed.

For a word \(y\), decompose it into maximal constant runs. Write \(A(y)\) for its number of runs of length at least four, and \(B(y)\) for the number of strictly interior runs of length exactly two whose immediately adjacent run symbols are equal. These are nonnegative integers.

## Proof
**1. Inverse-parent classification.** A valid inverse window has the form \(abba\). If \(a\ne b\), its central \(bb\) is a maximal interior run of length exactly two, and its two flanking symbols agree. Each such run contributes one parent. If \(a=b\), the window is contained in a constant run of length at least four. All valid inverse windows in one such run give the same parent. Two windows giving the same parent cannot lie in different constant runs, nor can a nonconstant \(abba\) window collide with a different window: reversing the same forward duplication from two positions would otherwise produce the same word, and the equality conditions for length-two palindromic duplications force the entire intervening source segment to be constant. This also follows directly by specializing the general collision equations (10)–(12) in [1] to length two. Hence
\[
L(y)=A(y)+B(y).
\]
Unlike the binary case, an arbitrary interior run of length two is not enough: its two neighboring run symbols must agree.

**2. Weighted run enumeration.** Let \(z\) mark word length and \(t\) mark inverse-parent count. A run of length other than two has length series
\[
R_0=z+z^3+\frac{t z^4}{1-z},
\]
where a run of length at least four contributes one parent; a run of length two has series \(R_1=z^2\), and put \(R=R_0+R_1\). The initial run has \(q\) color choices. Each next run differs in color from its predecessor. Once three consecutive run colors \(a,b,c\) are known, the middle run contributes an extra factor \(t\) exactly when it has length two and \(a=c\).

For the run-length categories \(0\) (not length two) and \(1\) (length two), the transition of appending a new run has matrix
\[
M=\begin{pmatrix}
(q-1)R_0&(q-1)R_1\\
(q-2+t)R_0&(q-2+t)R_1
\end{pmatrix}.
\]
Indeed, when the middle run has length two, one next-run color repeats the color before it and earns \(t\), while the other \(q-2\) colors earn one; otherwise there are \(q-1\) choices. This rank-one matrix has nonzero eigenvalue \((q-1)R_0+(q-2+t)R_1\). Summing all run counts (with one-run words separately) gives
\[
F_q=qR+\frac{q(q-1)R^2}{1-(q-1)R_0-(q-2+t)R_1}
=\frac{qR(1-(t-1)z^2)}{1-(q-1)R-(t-1)z^2}.
\]
Because \(R=\bigl(z+(t-1)z^4\bigr)/(1-z)\), cancellation yields exactly the displayed rational function. This proves the coefficient formula for every \(q,N,j\), including zero-parent outputs.

**3. Mean and fluctuations.** Differentiate \(F_q(z,t)\) at \(t=1\), where \(F_q(z,1)=qz/(1-qz)\), and extract coefficients to obtain the stated exact mean for \(N\ge4\). Write
\[
H(z,t)=1-qz-(t-1)D_q(z),\qquad D_q(z)=z^2-z^3+(q-1)z^4.
\]
The equation \(H(\rho(t),t)=0\) has a unique positive analytic branch near \(t=1\), with \(\rho(1)=1/q\) and nonzero residue. Other poles are separated from \(1/q\) for \(t\) sufficiently close to one. Consequently the logarithmic moment-generating function has the local uniform expansion
\[
\log\mathbb E e^{sL(Y_N)}=N\log\frac{\rho(1)}{\rho(e^s)}+O_q(1),
\]
with the error analytic in a fixed neighborhood of zero (and exponentially small after the explicit analytic prefactor is extracted). Implicit differentiation gives
\[
\rho_t(1)=-\frac{D_q(1/q)}q,
\qquad\rho_{tt}(1)=\frac{2D'_q(1/q)D_q(1/q)}{q^2}.
\]
The first two derivatives at \(s=0\) of \(\log(\rho(1)/\rho(e^s))\) are respectively \(\mu_q\) and \(\nu_q\). The latter is strictly positive for \(q\ge2\). Taking \(s\) of order \(N^{-1/2}\) and using the analytic Taylor expansion proves the stated Gaussian limit and linear variance asymptotic.

**4. Reverse-complement transfer.** For duplication length two, complementing precisely the odd zero-based positions of every word conjugates an ordinary palindromic duplication to a reverse-complement duplication, for any involutive complement [2, Section 4]. The conjugacy bijects complete receiver spaces and their parent sets at both lengths. Hence the inverse-list histogram, all its moments, and its limit law are unchanged.

## Verification
Run `python3 verify.py` in a directory containing the supplied standalone script. It independently constructs every valid palindrome window, reconstructs the distinct parents, and compares the resulting histogram to coefficients computed from the rational-function identity using integer-polynomial arithmetic, with no floating-point equality tests. It also checks the run classification, maximum list size, and exact mean. Verified ranges: \(q=2\) through length 12, \(q=3\) through length 9, \(q=4\) through length 8, and \(q=5\) through length 7; 222,456 words at lengths at least four were checked. The run yields `VERIFY_OK`. These finite tests corroborate but do not replace the proof for unbounded lengths.

## Relationship to prior work
Lenz, Wachter-Zeh and Yaakobi [1] proved collision identities for palindromic operations, gave the binary length-two palindromic-deletion sphere formula, and enumerated the corresponding binary sphere-size populations. Those binary results are not claimed anew. Earlier inverse-list extremal and incidence formulas already cover the sharp maximum and mean; neither extremal count nor aggregate incidence is presented as an independent advance here. The new precise content is the all-alphabet rational population law, which for \(q\ge3\) depends on returns to the previous run color and is not obtained by substituting \(q\) into the binary run histogram, together with the explicit nondegenerate normal limit.

Zabokritskiy [2] studies sequential palindromic and reverse-complement errors, proves their even-length conjugacy and bounds inverse lists; its main exact sphere theorem concerns two forward operations rather than the nonbinary inverse-list population of one operation. Sun and Ge [3] study codes and redundancy under related duplication channels. The reverse-complement statement here is a transfer using the established conjugacy, not a separately invented equivalence.

## Limitations
The result concerns exactly one fixed length-two duplication, not arbitrary lengths or two sequential errors. Uniform choice over all receivers is different from a channel-output distribution generated by a uniform source. The theorem determines receiver ambiguity distributions, but does not itself establish optimal correcting-code cardinalities or efficient encoders. Earlier binary and extremal results are acknowledged. The novelty assessment is based on inspected relevant sources and indexed searches, not a proof that no equivalent nonbinary formulation exists elsewhere. No independent external audit has been performed.

## References
[1] A. Lenz, A. Wachter-Zeh, E. Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, arXiv:1707.00052 (first public 2017-06-30), Sections 3.3, 3.4, 4.2, Appendix 0.A. https://arxiv.org/abs/1707.00052

[2] A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779 (first public 2026-09-01), Sections 4–6. https://arxiv.org/abs/2609.00779

[3] Y. Sun, G. Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151 (first public 2026-02-01), Sections III–V. https://arxiv.org/abs/2602.01151
