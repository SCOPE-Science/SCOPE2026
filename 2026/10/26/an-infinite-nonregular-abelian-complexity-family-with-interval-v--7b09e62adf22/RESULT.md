# An infinite nonregular abelian-complexity family with interval-valued power-scale limits

## Finding
For every integer \(r\ge4\), let \(\sigma_r\) act on \(\mathbb Z/3\mathbb Z\) by \(\sigma_r(a)=a^r(a+1)\), with addition modulo three and \(a^r\) denoting \(r\) repetitions of \(a\). Put \(k=r+1\). Its one-sided fixed point \(s_r=\lim_{m\to\infty}\sigma_r^m(0)\) exists, and let \(b_r\) be the binary coding which outputs one at a zero of \(s_r\), and zero otherwise. Let \(P_r(n)\) count the distinct Parikh vectors of length-\(n\) factors of \(b_r\).

Define \(\omega=\exp(2\pi i/3)\), \(\lambda=r+\omega\), \(\varrho=|\lambda|=\sqrt{r^2-r+1}\), \(\theta=\arg\lambda\), and the continuous \(2\pi\)-periodic function
\[
\Phi(x)=\max_{a\in\{0,1,2\}}\cos(x-2\pi a/3)-\min_{a\in\{0,1,2\}}\cos(x-2\pi a/3).
\]
The uniformly convergent series
\[
H_r(x)=\frac{2r}{3}\sum_{j=1}^{\infty}\varrho^{-j}\Phi(x-j\theta)
\]
is positive, continuous, and nonconstant. The exact power-length formula is
\[
\boxed{P_r(k^m)=\varrho^mH_r(m\theta)+2-H_r(0)}\qquad(m\ge0).
\]
Equivalently, writing \(N_m(a)=|\sigma_r^m(0)|_a\) and \(g_m=\max_aN_m(a)-\min_aN_m(a)\),
\[
P_r(1)=2,\qquad P_r(k^{m+1})-P_r(k^m)=r g_m=\frac{2r}{3}\varrho^m\Phi(m\theta).
\]
The normalized sequence \(P_r(k^m)/\varrho^m\), as \(m\to\infty\), has precisely the nondegenerate closed interval \([\min H_r,\max H_r]\) as its set of subsequential limits. In particular \(P_r\) is not \(k\)-regular, although \(b_r\) is \(k\)-automatic. For every integer \(e\ge3\), taking \(r=2^e-1\) gives a different \(2\)-automatic binary sequence whose abelian complexity is not \(2\)-regular.

## Assumptions and scope
The alphabet is always exactly \(\mathbb Z/3\mathbb Z\). The parameter \(r\) is an integer at least four and is independent of the alphabet size. A factor is contiguous; Parikh vectors of binary factors are determined by their number of ones. The complexity \(P_r(n)\) is defined for all positive lengths, but the formula describes only the lengths \(n=k^m\). Regularity means finite-dimensional span, over \(\mathbb Q\), of the base-\(k\) kernel. The endpoints of the accumulation interval are exact extrema of an explicitly uniformly convergent series; no elementary endpoint constants are asserted.

## Proof
**1. Adjacent-letter coverage and exact weighted-factor recurrence.** The fixed point contains all three letters because \(\sigma_r^2(0)\) contains \(0,1,2\). Once each letter \(a\) occurs, the images \(\sigma_r(a)\) exhibit adjacent pairs \(aa\) and \(a(a+1)\). Images of the adjacent pair \(aa\) exhibit \((a+1)a\) at the junction. These nine pairs exhaust the ordered pairs of the ternary alphabet. Each consequently occurs in \(s_r\).

Give letters arbitrary real additive weights \(w(a)\). Write \(U_{m,a}=\sigma_r^m(a)\), \(W_m(a)=w(U_{m,a})\), and let \(T_m\) be the maximum weight of a length-\(k^m\) factor of \(s_r\). We prove, for every \(m\ge0\),
\[
T_{m+1}=T_m+r\max_aW_m(a).\tag{1}
\]
For the upper bound, split a length-\(k^{m+1}\) factor by consecutive length-\(k^m\) substitution blocks. It is a suffix of a block, followed by \(r\) complete blocks, followed by a prefix of a last block. The suffix and last prefix together have total length \(k^m\) and are a factor of \(s_r\), since every ordered pair of block labels occurs. Their total weight is at most \(T_m\), and the remaining complete blocks have weight at most \(r\max_aW_m(a)\). The same argument permits an empty final prefix.

For the lower bound choose maximizing letters \(c_m\) for \(W_m\) inductively. If \(c\) maximizes \(W_m\), then, using \(W_{m+1}(a)=rW_m(a)+W_m(a+1)\),
\[
W_{m+1}(c)-W_{m+1}(c+1)=(r-1)(W_m(c)-W_m(c+1))+(W_m(c)-W_m(c-1))\ge0.
\]
Thus a maximizing \(c_{m+1}\) can always be selected in \(\{c_m-1,c_m\}\). We simultaneously maintain that a length-\(k^m\) factor attaining \(T_m\) starts in the first block of either \(U_{m,c_m-1}U_{m,c_m}\) or \(U_{m,c_m}U_{m,c_m+1}\). At \(m=0\) the single letter \(c_0\) does so. For the induction step write \(c=c_m\), \(U_a=U_{m,a}\) and \(L=k^m\). The occurring pair of expanded blocks has the decomposition
\[
\sigma_r^{m+1}(c-1)\sigma_r^{m+1}(c)=U_{c-1}^{r}U_c^{r+1}U_{c+1}.\tag{2}
\]
If the old maximizing factor consists of a suffix of \(U_{c-1}\) and a prefix of \(U_c\), place its suffix in the last \(U_{c-1}\), insert \(r\) full \(U_c\)'s, and take its prefix in the next \(U_c\). If instead it consists of a suffix of \(U_c\) and a prefix of \(U_{c+1}\), use the first \(U_c\) in the displayed run for its suffix, the next \(r\) copies for the full blocks, and the prefix of \(U_{c+1}\). Each yields an occurring factor of length \((r+1)L\), weight \(T_m+rW_m(c)\), starting in the first of the expanded blocks in (2). As \(c_{m+1}\in\{c-1,c\}\), this also preserves the claimed neighboring-block invariant. Empty prefixes are allowed, and the starting suffix is nonempty. This proves (1) for arbitrary weights and all \(r\ge4\).

**2. Binary abelian-complexity recurrence.** Let \(M_m\) and \(L_m\) respectively be the maximum and minimum counts of zeros of \(s_r\) among factors of length \(k^m\). Apply (1) first with \(w(0)=1\), other weights zero, and then with \(w(0)=-1\), other weights zero. The substitution commutes with cyclic relabeling, so the zero-counts of \(\sigma_r^m(a)\), as \(a\) varies, are just \(N_m(0),N_m(1),N_m(2)\) in some order. Hence
\[
M_{m+1}=M_m+r\max_aN_m(a),\qquad L_{m+1}=L_m+r\min_aN_m(a).
\]
Sliding a window across a binary word changes its one-count by at most one, and every intermediate count between the attained minimum and maximum appears. Thus \(P_r(k^m)=M_m-L_m+1\). With \(P_r(1)=2\), subtraction yields the stated recurrence exactly.

**3. Cyclic spectral formula.** Block counts obey \(N_0=(1,0,0)\) and \(N_{m+1}(a)=rN_m(a)+N_m(a-1)\). Therefore
\[
\sum_aN_m(a)=k^m,\qquad\sum_a\omega^aN_m(a)=\lambda^m.
\]
Discrete Fourier inversion gives, for each \(a\in\{0,1,2\}\),
\[
N_m(a)=\tfrac13\bigl(k^m+2\varrho^m\cos(m\theta-2\pi a/3)\bigr).
\]
It follows that \(g_m=(2/3)\varrho^m\Phi(m\theta)\). Since \(\varrho>1\), the displayed series for \(H_r\) converges uniformly. Index shifting verifies the functional equation
\[
\varrho H_r(x+\theta)-H_r(x)=\tfrac{2r}{3}\Phi(x).\tag{3}
\]
The recurrence and initial value, together with (3), establish the exact formula for \(P_r(k^m)\) by induction.

**4. Irrational phase and full limit interval.** For \(r\ge4\), \(0<2\theta<\pi/3\). If \(\theta/\pi\) were rational, \(\lambda/\overline\lambda=e^{2i\theta}\) would be a root of unity in \(\mathbb Q(\omega)\). The only roots of unity in this quadratic field are \(\{\pm1,\pm\omega,\pm\omega^2\}\), and none has argument strictly between zero and \(\pi/3\). So \(\theta/\pi\) is irrational. The function \(\Phi\) is nonconstant (for example \(\Phi(0)=3/2\), \(\Phi(\pi/6)=\sqrt3\)). If \(H_r\) were constant, (3) would make \(\Phi\) constant, which is false. Therefore \(H_r\) is a continuous nonconstant periodic function with a nondegenerate interval as its image. Irrational rotation makes \(m\theta\pmod{2\pi}\) dense, and \((2-H_r(0))\varrho^{-m}\to0\), proving the exact accumulation set.

**5. Nonregularity.** Suppose the sequence \(P_r(n)\) were \(k\)-regular. Its finite-dimensional kernel representation implies that \(A_m=P_r(k^m)\) is a constant-coefficient linear-recurrence sequence (one repeatedly applies the digit-zero transition to the finite kernel span). Consequently \(g_m=(A_{m+1}-A_m)/r\) is also a linear-recurrence sequence. But \(g_m=(2/3)\varrho^m\Phi(m\theta)\), so the bounded sequence \(\Phi(m\theta)\) would satisfy a constant-coefficient linear recurrence. Every bounded complex constant-coefficient linear-recurrence sequence has the form \(\sum_{j=1}^{d}c_jz_j^m+o(1)\), with finitely many distinct \(|z_j|=1\). For each integer \(\ell\), unique ergodicity of irrational circle rotation and the geometric-series mean give
\[
\lim_{N\to\infty}\frac1N\sum_{m=0}^{N-1}\Phi(m\theta)e^{-i\ell m\theta}=\widehat\Phi(\ell).
\]
The analogous limit for a finite exponential sum vanishes unless some \(z_j=e^{i\ell\theta}\). As \(\theta/(2\pi)\) is irrational, this can happen for only finitely many integers \(\ell\). Thus \(\Phi\) would have finitely supported Fourier series and, by uniqueness of Fourier coefficients for continuous functions, would be a trigonometric polynomial. Yet at \(x=0\), the minimum defining \(\Phi\) switches between two cosine branches with different derivatives while its maximum branch is unique. So \(\Phi\) is not differentiable at zero, unlike every trigonometric polynomial. Contradiction.

The sequence \(b_r\) is \(k\)-automatic as a coding of a fixed point of a \(k\)-uniform substitution. For \(r=2^e-1\), \(k=2^e\), and base-power invariance of automaticity and regularity gives \(2\)-automaticity and failure of \(2\)-regularity. Different \(r\) produce different binary words because the first zero in \(b_r\) occurs after the initial run of \(r\) ones, at index \(r\).

## Verification
The standalone Python 3 script `verify_cyclic_abelian.py` constructs substitution blocks directly, first verifies all nine adjacent ordered pairs occur, then independently takes minimum and maximum zero counts across every length-\(k^m\) sliding window of all nine ordered pairs of \(m\)-level substitution blocks. It checks the predicted recurrence without using the weighted-factor proof. Values \(r=3,4,5,6,7,15\) and \(m=0,1,2,3,4\) give 30 exact integer comparisons. The case \(r=3\) calibrates against the published example; the five other parameters test new members. The recorded output reports PASS. These finite tests do not prove the infinite theorem, for which the preceding argument is essential.

## Relationship to prior work
Allouche, Rampersad, Rigo, Shallit, and Stipulanti (arXiv:2610.03837, first posted October 2, 2026) prove nonregularity for the single substitution \(a\mapsto a^3(a+1)\) on three letters and its binary coding, and their Lemma 9 supplies the model for a weighted-factor induction. Their Remark 4 explicitly raises other exponents and alphabets as a question. The present claim treats every exponent \(r\ge4\) with a fixed three-symbol alphabet, supplies an exact uniformly convergent phase function, proves a full nondegenerate limit interval, and gives infinitely many distinct binary automatic examples. The published single-parameter result does not imply these statements without additional arguments.

Couvreur and collaborators (arXiv:2504.13584, 2025) give effective abelian-complexity results for Pisot-type substitutions. Here the incidence matrix has non-Perron eigenvalues \(r+\omega\) and \(r+\overline\omega\), both of modulus \(\sqrt{r^2-r+1}>1\), so those Pisot-type hypotheses are not satisfied. Other published complexity results for Sturmian and generalized Thue–Morse families concern different substitution systems and do not supply this claim. Originality is asserted relative to the materials inspected, not as a guarantee that no equivalent unindexed result exists.

## Limitations
Only the ternary substitution with exponent \(r\ge4\) and its indicated binary projection are treated. The theorem does not provide a closed expression for \(P_r(n)\) at arbitrary positive \(n\), does not determine the numerical extrema of \(H_r\) in elementary terms, and does not classify every alphabet size or cyclic substitution. The verification program checks finite instances only. Independent scientific validation has not been performed.

## References
1. J.-P. Allouche, N. Rampersad, M. Rigo, J. Shallit, M. Stipulanti, *An example of an automatic sequence with non-regular abelian complexity*, arXiv:2610.03837, first posted 2026-10-02; especially Sections 2–4, Lemma 9, and Remark 4. https://arxiv.org/abs/2610.03837
2. J. Couvreur, M. Delacourt, N. Ollinger, P. Popoli, J. Shallit, M. Stipulanti, *Effective computation of generalized abelian complexity for Pisot type substitutive sequences*, arXiv:2504.13584, first posted 2025-04-22. https://arxiv.org/abs/2504.13584
3. J.-P. Allouche and J. Shallit, *The ring of \(k\)-regular sequences*, Theoretical Computer Science 98 (1992), 163–197.
4. J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press, 2003.
