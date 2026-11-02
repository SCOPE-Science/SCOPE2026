# Non-regular abelian complexity for an infinite odd-repetition family of ternary morphisms

## Finding
For every odd integer \(r\ge5\), let \(\sigma_r\) be the constant-length \(r+1\) substitution on \(\mathbb Z/3\mathbb Z\) given by
\[
\sigma_r(a)=a^r(a+1\pmod3).
\]
Let \(s_r=\sigma_r^\infty(0)\), and let \(b_r\) be the binary sequence obtained by coding \(0\mapsto1\) and \(1,2\mapsto0\). Then \(b_r\) is \((r+1)\)-automatic, but its abelian complexity \(\rho^{\mathrm{ab}}_{b_r}\) is **not** \((r+1)\)-regular.

More precisely, let \(N_0=(1,0,0)\), \(N_{m+1}(a)=rN_m(a)+N_m(a-1\pmod3)\), and \(g_r(m)=\max_a N_m(a)-\min_aN_m(a)\). For every \(m\ge0\),
\[
\rho^{\mathrm{ab}}_{b_r}((r+1)^m)=2+r\sum_{j=0}^{m-1}g_r(j).
\]
The sequence of these values modulo \(2\) is not eventually periodic.

## Assumptions and scope
The alphabet consists of three *distinct* letters \(0,1,2\); substitutions use arithmetic modulo \(3\). The repetition \(r\) is an arbitrary fixed odd integer at least \(5\); the base is \(k=r+1\). Factor languages are taken from the one-sided infinite fixed point. Abelian complexity counts the distinct Parikh vectors of factors of a given length. No claim is made here for even \(r\), variable alphabets, or other binary codings. The case \(r=3\) is previously established, not a novel instance.

## Proof
**1. Complete adjacency.** The fixed point contains all three letters: \(\sigma_r^2(0)\) contains \(0,1,2\). Every \(aa\) and \(a(a+1)\) occurs in \(\sigma_r(a)\), since \(r\ge2\). Also \((a+1)a\) occurs across the boundary in \(\sigma_r(aa)\). Thus every ordered two-letter factor occurs in \(s_r\). In particular, every factor of length \(k^m\) is contained in \(\sigma_r^m(a)\sigma_r^m(b)\) for some two-letter factor \(ab\), and all nine such concatenations occur.

**2. Weighted-factor lemma.** Assign arbitrary real weights to the three letters. Write \(v_m(a)=\operatorname{wt}(\sigma_r^m(a))\), and \(H_m\) for the maximum weight of a factor of \(s_r\) of length \(k^m\). Then
\[
H_{m+1}=H_m+r\max_{a\in\mathbb Z/3\mathbb Z}v_m(a).\tag{1}
\]
For the upper bound, decompose a length-\(k^{m+1}\) factor into a suffix and prefix of two \(k^m\)-blocks and the intervening \(r\) complete blocks. The boundary pieces, concatenated, form a length-\(k^m\) factor because every ordered letter pair occurs, proving the upper bound.

For equality, use the cyclic boundary induction from the three-letter maximizing-factor argument of Allouche–Rampersad–Rigo–Shallit–Stipulanti (2026, Lemma 9). Here are the parameter-dependent steps, so that the extension does not assume the lemma at a new parameter. Choose a maximizing letter \(c\) for \(v_m\). The recursion \(v_{m+1}(a)=rv_m(a)+v_m(a+1)\) gives
\[
v_{m+1}(c)-v_{m+1}(c+1)
=(r-1)(v_m(c)-v_m(c+1))+(v_m(c)-v_m(c-1))\ge0.
\]
Thus a maximizing letter at the next level may be selected from \(\{c-1,c\}\); there is no fourth cyclic possibility. In the boundary induction, a length-\(k^m\) maximum-weight factor can be placed crossing either \(\sigma_r^m(c-1)|\sigma_r^m(c)\) or \(\sigma_r^m(c)|\sigma_r^m(c+1)\), with its initial position in the first block. Put \(U_a=\sigma_r^m(a)\). Both relevant boundary patterns occur in
\[
\sigma_r^{m+1}(c-1)\sigma_r^{m+1}(c)
=U_{c-1}^{\,r}U_c\,U_c^{\,r}U_{c+1}.
\]
In the first case, extend a suffix of \(U_{c-1}\) and a prefix of \(U_c\) by the intervening \(r\) copies of \(U_c\); in the second, extend a suffix of \(U_c\) and a prefix of \(U_{c+1}\) by the \(r\) copies of \(U_c\). Either produces a factor of length \(k^{m+1}\) and weight \(H_m+rv_m(c)\). The same two boundary placements propagate the induction, since the next maximizing index lies in \(\{c-1,c\}\). The base case is a maximum-weight letter and is immediate. This proves (1); all steps require only \(r\ge2\), not specifically \(r=3\).

**3. Exact complexity at substitution lengths.** Let \(M_n,L_n\) be the maximum and minimum numbers of ones in a length-\(n\) factor of \(b_r\). Sliding windows changes the count by at most one, so every count between these extremes occurs, giving \(\rho^{\mathrm{ab}}_{b_r}(n)=M_n-L_n+1\). Apply (1) to the indicator weight of letter \(0\), then to its negative. The three total weights of the images \(\sigma_r^m(a)\) are cyclic rotations of \(N_m=(|\sigma_r^m(0)|_a)_{a=0}^2\). Hence
\[
M_{k^{m+1}}-M_{k^m}=r\max N_m,
\quad L_{k^{m+1}}-L_{k^m}=r\min N_m.
\]
Since \(M_1-L_1+1=2\), the stated exact formula follows.

**4. Parity and an irrational rotation.** Let \(\omega=e^{2\pi i/3}\), \(\lambda=r+\omega=\sqrt{r^2-r+1}\,e^{i\theta}\). Fourier diagonalization of the ternary cyclic recurrence gives
\[
\sum_a N_m(a)\omega^a=\lambda^m,\qquad
N_m(a)=\frac{k^m+2|\lambda|^m\cos(m\theta-2\pi a/3)}3.
\]
Furthermore,
\[
\cos(2\theta)=1-\frac3{2(r^2-r+1)}.
\]
For \(r\ge5\), this rational number lies strictly between \(1/2\) and \(1\). The rational-cosine theorem therefore implies \(\theta/\pi\notin\mathbb Q\).

Because \(r\) is odd, the recurrence modulo \(2\) is \(N_{m+1}(a)\equiv N_m(a)+N_m(a-1)\). For all \(n\ge1\), \(N_{3n}\equiv(0,1,1)\pmod2\). At these indices the range \(g_r(3n)\) is even precisely when \(N_{3n}(0)\) lies strictly between the other two entries. Direct multiplication of their differences gives
\[
(N_m(0)-N_m(1))(N_m(0)-N_m(2))
=\frac{|\lambda|^{2m}}3(4\cos^2(m\theta)-1).
\]
No equality occurs at positive \(m\), because \(\theta/\pi\) is irrational. Consequently
\[
g_r(3n)\equiv0\pmod2\iff |\cos(3n\theta)|<\tfrac12.
\]
For every positive integer \(p\), the irrational rotation \((3pn\theta\bmod\pi)_{n\ge1}\) is dense, with both strict inequalities above occurring infinitely often. Therefore \(g_r(m)\bmod2\) cannot be eventually periodic with period \(p\), for any \(p\); the exact-complexity recurrence and oddness of \(r\) imply the same for \(\rho^{\mathrm{ab}}_{b_r}(k^m)\bmod2\).

**5. Regularity contradiction.** The fixed point of a \(k\)-uniform morphism, followed by a letter coding, is \(k\)-automatic. If its abelian complexity were \(k\)-regular, reduction modulo \(2\) would be \(k\)-automatic (the standard finite-ring reduction property of integer-valued regular sequences). For any \(k\)-automatic sequence, the subsequence at indices \(k^m\) is eventually periodic: its automaton reads \(1\) followed by \(m\) zeros, so iteration of the zero transition moves in a finite functional graph. This contradicts step 4, completing the proof.

## Verification
Run `python3 verify.py` using Python 3. The attached program independently enumerates all substitution-block boundary factors at selected parameters, compares their exact extrema with the cyclic-matrix recurrence, checks the parity/sign law with exact unbounded integers, and stress-tests the weighted-factor recursion. It reports 20 full factor-language cases, 700 parity/sign cases, and 162 weighted cases. These checks corroborate but are not substitutes for the all-parameter argument.

## Relationship to prior work
Allouche, Rampersad, Rigo, Shallit and Stipulanti (arXiv:2610.03837, publicly submitted 2026-10-02) prove the special \(r=3\) ternary morphism, including the weighted-factor lemma and irrational-rotation method; their Remark 4 asks about other repetitions and alphabets. The new theorem resolves the **whole infinite family of odd repetitions \(r\ge5\)** on a fixed ternary alphabet. It is not an instance of their fixed \(r=3\) statement, though it adapts its proof mechanism. Chen and Wen (arXiv:1809.06554) consider generalized Thue–Morse substitutions with eventually periodic complexity; their uniform cyclic increment has no repeated-letter block \(a^r\), and does not imply the claimed nonregularity.

## Limitations
No assertion is made about even repetition values or alphabets other than \(\mathbb Z/3\mathbb Z\), and the theorem does not calculate complexity for arbitrary lengths. Earlier unindexed generalizations cannot be definitively excluded by literature search.

## References
- J.-P. Allouche, N. Rampersad, M. Rigo, J. Shallit, and M. Stipulanti, *An example of an automatic sequence with non-regular abelian complexity*, arXiv:2610.03837v1 (2026), especially Lemma 9, Proposition 8, Lemmas 10–13, Proposition 14, and Remark 4, https://arxiv.org/abs/2610.03837.
- J. Chen and Z.-X. Wen, *On the abelian complexity of generalized Thue–Morse sequences*, arXiv:1809.06554 (2018), https://arxiv.org/abs/1809.06554.
- J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press (2003), results on finite-ring reductions of regular sequences.
