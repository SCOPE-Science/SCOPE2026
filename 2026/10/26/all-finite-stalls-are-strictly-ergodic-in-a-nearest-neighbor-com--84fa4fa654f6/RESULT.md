# All finite stalls are strictly ergodic in a nearest-neighbor compact-alphabet substitution

## Finding
Let \(m\ge1\) be any integer and let \(\mathcal A=\mathbb N_0\cup\{\infty\}\) carry the one-point compactification topology. Define a continuous substitution \(\rho_m\) by
\[
\rho_m(j)=
\begin{cases}
(j+1),&0\le j<m,\\
0\,(j-1)\,(j+1),&j\ge m,\\
0\,\infty\,\infty,&j=\infty.
\end{cases}
\]
Every \(\rho_m\) is primitive and its two-sided substitution subshift is **strictly ergodic** (minimal and uniquely ergodic). Its substitution operator on \(C(\mathcal A)\) has spectral radius \(\lambda_m>2\), determined exactly as follows. There is a unique \(s_m\in(0,1)\) satisfying
\[
(1-s_m)(s_m+s_m^{-1})^{m-1}=s_m^2,
\qquad \lambda_m=s_m+s_m^{-1}.
\]
The roots \(\lambda_m\) strictly decrease with \(m\) and obey the sharp asymptotic
\[
\lambda_m-2=4^{1-m}\bigl(1+O(2^{-m})\bigr)\quad(m\to\infty).
\]
In particular, the seven-stall substitution, for which non-unique ergodicity was explicitly conjectured in the motivating paper, is **uniquely ergodic**. Although its length after \(1000\) substitutions of the seed \(0\) is less than \(2^{1000}\), its length after \(72000\) substitutions is rigorously greater than \(2^{72000}\).

## Assumptions and scope
The integer \(m\) is finite and positive; \(j\) denotes a finite nonnegative alphabet letter. The expression \(0\,(j-1)\,(j+1)\) denotes a word of three letters, not a numerical product. The substitution at \(\infty\) is the continuous extension of the finite-letter rule as \(j\to\infty\). The subshift \(X_{\rho_m}\subset\mathcal A^{\mathbb Z}\) consists of bi-infinite configurations whose finite blocks are limits of blocks occurring in substituted words. The substitution operator is
\[
(M_m f)(j)=\sum_{a\text{ in the word }\rho_m(j)}f(a),
\qquad f\in C(\mathcal A).
\]
All operator norms below are supremum norms. The strict-ergodicity implication from quasi-compactness and primitivity is the existing compact-alphabet substitution theorem, not a new general theorem.

## Proof
**1. Unique spectral parameter.** Write \(\lambda(s)=s+s^{-1}\), \(s\in(0,1)\). The function \((1-s)\lambda(s)^{m-1}/s^2\) is continuous, strictly decreasing from \(+\infty\) to \(0\). It equals \(1\) at exactly one \(s=s_m\). Consequently \(\lambda_m>2\). For fixed \(s\), increasing \(m\) strictly increases this function, so the unique root \(s_m\) increases strictly with \(m\); thus \(\lambda_m\) decreases.

**2. Positive continuous eigenfunction.** Suppress the subscript \(m\), and put
\[
c=(\lambda-2)^{-1}=\frac{s}{(1-s)^2},\qquad
h(j)=\begin{cases}
\lambda^j,&0\le j<m,\\
c+(\lambda^m-c)s^{j-m},&j\ge m,\\
c,&j=\infty.
\end{cases}
\]
This defines a continuous function on the compact alphabet. The defining equation for \(s\) is algebraically equivalent to
\[
\lambda^m-c=s(\lambda^{m-1}-c).
\]
For \(j<m\), \((M_mh)(j)=h(j+1)=\lambda h(j)\). For \(j>m\), the identities \(s+s^{-1}=\lambda\) and \((\lambda-2)c=1\) yield
\[
1+h(j-1)+h(j+1)=\lambda h(j).
\]
The displayed interface identity makes this valid also at \(j=m\). At \(\infty\), \(1+2c=\lambda c\). Hence \(M_mh=\lambda h\) at every alphabet letter. Moreover,
\[
\frac c{\lambda^m}=\frac1{(1-s)(1+s^2)}>1.
\]
Thus \(h\) increases from \(h(0)=1\) toward \(h(\infty)=c\), and \(1\le h\le c\). In particular it is a strictly positive order unit.

**3. Exact spectral radius.** Positivity of \(M_m\) gives, for any \(f\in C(\mathcal A)\),
\[
|M_m^nf|\le M_m^n|f|\le\|f\|_\infty M_m^nh
=\|f\|_\infty\lambda^nh.
\]
Therefore \(\|M_m^n\|\le c\lambda^n\); the eigenfunction \(h\) supplies the reverse spectral-radius inequality. The spectral radius is exactly \(r(M_m)=\lambda\). Applying the inequalities \(h/c\le\mathbf1\le h\) also gives the useful all-time length bounds
\[
\frac{\lambda^n}{c}\le |\rho_m^n(0)|\le\lambda^n\qquad(n\ge0).
\]

**4. Explicit finite-rank decomposition.** Define a positive bounded operator \(S\) by \((Sf)(j)=0\) for \(j<m\), \((Sf)(j)=f(j-1)+f(j+1)\) for \(j\ge m\), and \((Sf)(\infty)=2f(\infty)\). Then \(\|S\|\le2\), and \(M_m-S\) has finite rank: its values on \(j<m\) are \(f(j+1)\), and its value at every \(j\ge m\) and at \(\infty\) is \(f(0)\). Consequently \(T=M_m/\lambda\) has spectral radius \(1\) and differs from the finite-rank (hence compact) operator \((M_m-S)/\lambda\) by operator norm at most \(2/\lambda<1\). This directly proves quasi-compactness in the standard definition.

**5. Primitivity and strict ergodicity.** For each finite seed, letters below \(m\) progress upward until reaching \(m\), while letters at least \(m\) retain an at-least-\(m\) descendant through the successor branch. Thus every finite seed has such a descendant by time \(m\), and its later superwords contain \(0\) at every time at least \(m+1\). The superwords of \(\infty\) contain \(\infty\) and therefore also \(0\) at every positive time. Consequently all seeds contain \(0\) after the same number \(m+1\) of substitutions and at every subsequent time. For any specified finite letter \(k\), continuing the chain \(0\mapsto1\mapsto\cdots\mapsto k\) shows that some common iterate of every seed contains \(k\). Every nonempty open subset of \(\mathcal A\) contains an isolated finite letter, so \(\rho_m\) is primitive. The established compact-alphabet theorem that primitive quasi-compact substitutions generate minimal uniquely ergodic subshifts now applies [1, Theorem 1.2; 2, Theorem 6.7].

**6. Sharp gap asymptotic.** The defining equation gives \(\delta_m=1-s_m=s_m^2/\lambda_m^{m-1}\le2^{1-m}\). Thus \(\delta_m=O(2^{-m})\) and \(\lambda_m-2=\delta_m^2/s_m=O(4^{-m})\). Substituting back yields \(\delta_m=2^{1-m}(1+O(2^{-m}))\), and hence \(\lambda_m-2=4^{1-m}(1+O(2^{-m}))\).

**7. A finite reversal certificate at seven stalls.** The rational \(s_*=9848553/10000000\) has \((1-s_*)(s_*+s_*^{-1})^6-s_*^2<0\). Monotonicity therefore gives \(s_7<s_*\), hence the exact inequalities \(\lambda_7>200023288/100000000=2.00023288\) and \(c_7<4300\). With \(x=11644/100000000\), exact rational arithmetic verifies
\[
\sum_{j=0}^{15}\binom{72000}{j}x^j>4300.
\]
By the binomial theorem and the length lower bound,
\[
|\rho_7^{72000}(0)|\ge\lambda_7^{72000}/c_7
>2^{72000}(1+x)^{72000}/4300>2^{72000}.
\]
Separately, direct integer recurrence gives \(|\rho_7^{1000}(0)|<2^{1000}\). This explains why a long finite calculation can misleadingly suggest a growth rate below two despite \(r(M_7)>2\).

## Verification
Run `python3 verify.py` from this directory with the standard-library Python interpreter. The verifier performs 1,101 exact-rational, high-precision, and finite-integer checks, including bracketed roots for \(1\le m\le20\), substitution-operator recurrence residuals, direct small-word expansion, the previously reported length \(|\rho_2^{34}(0)|=17598130109\), the seven-stall 1000-step inequality, and the rational 72000-step certificate. These checks corroborate the proof; finite sample calculations alone do not establish the universal theorem. All proof lemmas are stated above and require no external code.

## Relationship to prior work
Walton [1, Section 4.1] proves unique ergodicity for the two-stall nearest-neighbor version by a finite growth check, gives a four-stall growth check, and explicitly conjectures **non-unique** ergodicity for the seven-stall version after observing its apparent growth rate below two through 1000 iterations. The present exact positive eigenfunction resolves that stated conjecture in the opposite direction, and treats all finite stall lengths simultaneously. The main non-uniquely ergodic example in [1] instead uses the genuinely different rule \(j\mapsto0\,(j-2)\,(j+1)\) after two stalls; it is not covered by this claim. The dynamical implication from quasi-compactness and primitivity is supplied by the general theory in [1, 2]. The new contribution is the explicit sharp spectral calculation and the all-stall classification, not a new general Perron-Frobenius theorem.

## Limitations
This theorem concerns exactly the nearest-neighbor tail rule and **finite** stall length. It does not classify asymmetric jumps, the \(j-2\) rule, arbitrary countable-alphabet substitutions, or invariant-measure ergodic decompositions for other examples. The spectral calculation and finite-growth comparison are analytically proved here, but independent external validation and a fully exhaustive historical-priority determination have not been performed. No finite numerical experiment is treated as an infinite proof.

## References
[1] J. J. Walton, *Unique ergodicity, and not, for primitive substitutions on compact alphabets containing isolated points*, arXiv:2609.07550v1 (first public version, 7 September 2026), especially Sections 1, 4.1, and 5. https://arxiv.org/abs/2609.07550

[2] N. Mañibo, D. Rust, and J. J. Walton, *Substitutions on compact alphabets*, Journal of the London Mathematical Society 111 (2025), article e70123, DOI:10.1112/jlms.70123; first arXiv version 15 April 2022, arXiv:2204.07516. https://arxiv.org/abs/2204.07516
