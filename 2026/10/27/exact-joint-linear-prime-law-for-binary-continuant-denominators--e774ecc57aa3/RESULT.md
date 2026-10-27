# Exact joint linear-prime law for binary continuant denominators

## Finding

Let \(\mathbb F_2[T]\) be the polynomial ring over the two-element field. For a word \(w=(a_1,\ldots,a_d)\in\{T,T+1\}^{d}\), define its continuant by \(K_{-1}=0\), \(K_0=1\), and \(K_j=a_jK_{j-1}+K_{j-2}\) for \(1\le j\le d\). Put
\[
J_d=\#\{w\in\{T,T+1\}^{d}:\gcd(K_d(w),T(T+1))=1\}.
\]
For every integer \(m\ge0\), the exact joint root-avoidance counts are
\[
\boxed{J_{2m}=\frac{4\cdot4^m+4+(-2)^m}{9},\qquad
J_{2m+1}=\frac{4(2\cdot4^m-1-(-2)^m)}9.}
\]
For each \(d\ge0\), the number of words with \(K_d(w)(0)=1\) is equal to the number with \(K_d(w)(1)=1\), and both equal
\[
L_d=\frac{2^{d+1}+(-1)^d}{3}.
\]
Consequently the exact numbers of words according to their ordered evaluation pair \((K_d(w)(0),K_d(w)(1))\) are
\[
N_{11}(d)=J_d,\quad N_{10}(d)=N_{01}(d)=L_d-J_d,\quad
N_{00}(d)=2^d-2L_d+J_d.
\]
For a uniform word, the two indicators of avoidance of the linear primes \(T\) and \(T+1\) converge to independent Bernoulli variables with success parameter \(2/3\):
\[
\lim_{d\to\infty}\Pr(T\nmid K_d(w),\ T+1\nmid K_d(w))=\frac49.
\]
This convergence has an exact oscillatory second term of order \(2^{-d/2}\). Writing \(X_d=\mathbf1_{T\nmid K_d(w)}\), \(Y_d=\mathbf1_{T+1\nmid K_d(w)}\), the exact covariances are
\[
\operatorname{Cov}(X_{2m},Y_{2m})
=\frac{(-2)^m}{9\cdot4^m}-\frac1{9\cdot16^m},
\qquad
\operatorname{Cov}(X_{2m+1},Y_{2m+1})
=-\frac{2(-2)^m}{9\cdot4^m}-\frac1{36\cdot16^m}.
\]
In particular the sign of the covariance alternates with successive even degrees and also with successive odd degrees, apart from the zero covariance at degree zero.

This is a law in the natural *orthogonal-multiplicity-weighted* ensemble of degree-\(d\) monic polynomials: choosing \(f\) with probability \(m(f)/2^d\), where \(m(f)\) counts degree-one-partial-quotient continued fractions with denominator \(f\), gives the same evaluation-pair law as choosing a uniform word. It must not be confused with uniform sampling of monic polynomials, for which the probability of avoiding both linear factors is exactly \(1/4\) when \(d\ge2\).

## Assumptions and scope

Every polynomial coefficient and continuant recurrence is interpreted in characteristic two; all counting and transfer matrices below are over the ordinary integers, not reduced modulo two. A word has ordered letters, and words yielding the same continuant polynomial are counted with their multiplicity. The empty word \(d=0\) is included to initialize the recurrence. All formulas are unconditional, for every stated integer degree. The association of word multiplicities to the standard orthogonal multiplicity \(m(f)\) uses the continued-fraction bijection recorded in the references; the numerical counts themselves follow directly from the given recurrence.

## Proof

**1. Two-point transfer.** Evaluation of a binary polynomial at either \(0\) or \(1\) takes values in \(\mathbb F_2\). Two consecutive continuants cannot evaluate to zero simultaneously: the recursion can be inverted, and its initial pair is \((1,0)\). Thus each evaluation-state pair is in
\[
E=\{(1,0),(0,1),(1,1)\}.
\]
Order the nine product states \(E\times E\) lexicographically, with the first pair representing values at zero and the second representing values at one. For \((u,v,x,y)\in E\times E\), adjoining the letter \(T+\varepsilon\), with \(\varepsilon\in\{0,1\}\), acts as
\[
(u,v,x,y)\longmapsto
(\varepsilon u+v,u,(1-\varepsilon)x+y,x),
\]
with these additions interpreted in \(\mathbb F_2\). Let \(M\) be the integer \(9\)-by-\(9\) matrix counting the two transitions from each input state to each output state. If \(v_d\) is the column vector of state counts after \(d\) letters, then \(v_{d+1}=Mv_d\), and the initial vector is \(v_0=(1,0,0,0,0,0,0,0,0)^\mathsf{T}\).

Direct application of the displayed two-transition rule gives the following five vectors, in the specified state order:
\[
\begin{aligned}
v_0&=(1,0,0,0,0,0,0,0,0)^\mathsf T,\\
v_1&=(0,0,0,0,0,1,0,1,0)^\mathsf T,\\
v_2&=(0,1,1,1,0,0,1,0,0)^\mathsf T,\\
v_3&=(0,1,1,1,2,0,1,0,2)^\mathsf T,\\
v_4&=(4,1,1,1,2,2,1,2,2)^\mathsf T.
\end{aligned}
\]
They satisfy the **vector identity**
\[
v_4=v_3+2v_1+4v_0.
\]
Applying \(M^d\) yields \(v_{d+4}=v_{d+3}+2v_{d+1}+4v_d\) for every \(d\ge0\), so the same scalar recurrence holds for each sum of state coordinates. The count \(J_d\) is the sum over the four states whose first coordinates \(u\) and \(x\) are both \(1\), since these are exactly the continuants avoiding both linear factors. From the vectors one reads \((J_0,J_1,J_2,J_3)=(1,0,2,4)\). The recurrence therefore gives
\[
\sum_{d\ge0}J_d z^d=\frac{1-z+2z^2}{1-z-2z^3-4z^4}
=\frac{1-z+2z^2}{(1-2z)(1+z)(1+2z^2)}.
\]
Extracting the even and odd coefficients proves the displayed formulas for \(J_{2m}\) and \(J_{2m+1}\). These are integer counts by their construction, despite the denominators in the closed forms.

**2. Each marginal.** At either fixed evaluation point, the two equally represented letter evaluations are \(0\) and \(1\). On the ordered three states \(E\), the transfer matrix is
\[
B=\begin{pmatrix}0&2&0\\1&0&1\\1&0&1\end{pmatrix}.
\]
Writing \(e=(1,0,0)^\mathsf T\), one verifies \(B^2e=Be+2e\), so by the same commutation argument the marginal count obeys \(L_{d+2}=L_{d+1}+2L_d\) with \((L_0,L_1)=(1,1)\). Solving gives \(L_d=(2^{d+1}+(-1)^d)/3\). Interchanging the letters interchanges evaluation at zero and one, so the two marginal counts are equal. Inclusion–exclusion now gives the entire joint table.

**3. Limiting law and covariance.** Divide the exact counts by \(2^d\). In both parities \(L_d/2^d\to2/3\) and \(J_d/2^d\to4/9\); thus the limiting joint probabilities are precisely the products of the limiting marginal Bernoulli probabilities. The oscillatory pieces \((-2)^m\) in the closed forms have magnitude \(2^m\), whereas the main terms have magnitude \(4^m\). Hence the convergence error is of order \(2^{-d/2}\), and this order is attained along each fixed parity as \(m\to\infty\). Substituting the exact expressions into \(\operatorname{Cov}(X_d,Y_d)=J_d/2^d-(L_d/2^d)^2\) gives the two displayed exact covariance identities.

**4. Weighted versus uniform denominators.** For \(d\ge1\), every degree-one-partial-quotient rational function corresponds to one word, and the number with monic denominator \(f\) is \(m(f)\). Therefore \(\sum_{\deg f=d}m(f)=2^d\); the word law is exactly the weighted polynomial law. By contrast, for a uniformly selected monic polynomial of degree \(d\ge2\), the constant and linear coefficients are independently uniform binary bits. These give \(f(0)\) and, by an invertible affine change of variables, \(f(1)\). Thus its joint avoidance probability is \(1/4\), not \(4/9\).

## Verification

The accompanying standalone \(\texttt{verify.py}\) constructs both transfer rules with integer arithmetic and checks the crucial vector identity \(v_4=v_3+2v_1+4v_0\) exactly. It checks the resulting joint and marginal formulas and total mass for all degrees \(0\le d<100\). Independently of the transfer matrix, it enumerates every binary word of degree \(0\le d\le14\), computes its full polynomial continuant as a bit polynomial, and tests the two evaluations directly. Run `python3 verify.py`; the expected final line begins `VERIFY_OK`. These finite tests corroborate the exact symbolic argument; the proof of the all-degree claims is the transition identity and recurrence, not a bounded enumeration.

## Relationship to prior work

Niedbala Giraudin (2026), arXiv:2610.02352v1, defines orthogonal multiplicity, gives the word-to-denominator count and an exact formula for the **unweighted** number of monic polynomials having positive multiplicity, and analyzes residue invariants at non-linear irreducible factors. Its discussion of the two degree-one places is part of an Euler-product normalization. That work neither gives this weighted two-linear-factor joint table nor the finite-degree oscillating covariance; the present result is independent of its conjectural independence input.

Lauder (1998) studies which denominators have odd orthogonal multiplicity and their recursive structure, not the present two-evaluation distribution. Allouche–Han–Niederreiter (2020) explain the connection with perfect linear complexity profiles and automatic/apwenian sequences, rather than joint factor-avoidance counts in finite continuants. The 1999 Lauder study of prescribed partial-quotient alphabets is a plausible general structural antecedent whose complete content could not be compared here; this leaves a bibliographic priority risk. A sufficiently general unpublished or unindexed transfer-matrix theorem might also imply the result. Priority is not independently certified.

## Limitations

The probability law is weighted by orthogonal multiplicity, not a uniform law on monic degree-\(d\) polynomials. No claim is made about the asymptotic proportion of polynomials with positive orthogonal multiplicity, the distribution of non-linear irreducible factors, or independence over an arbitrary growing collection of primes. The covariance is a precise two-linear-prime phenomenon. The proof is self-contained modulo the standard word/denominator identification used solely in the weighted interpretation. No independent external audit has been undertaken.

## References

1. D. Niedbala Giraudin, *The proportion of polynomials over \(\mathbb F_2\) with positive orthogonal multiplicity*, arXiv:2610.02352v1, first posted 1 October 2026, https://arxiv.org/html/2610.02352v1.
2. A. G. B. Lauder, *Polynomials with odd orthogonal multiplicity*, Finite Fields and Their Applications 4 (1998), 453–464, author-hosted full text https://people.maths.ox.ac.uk/lauder/papers/Lauder_FF98.pdf.
3. J.-P. Allouche, G.-N. Han, H. Niederreiter, *Perfect linear complexity profile and Apwenian sequences*, Finite Fields and Their Applications 68 (2020), 101761, https://arxiv.org/html/2008.12160v1.
4. A. G. B. Lauder, *Continued fractions of Laurent series with partial quotients from a given set*, Acta Arithmetica 90 (1999), 251–271, DOI:10.4064/aa-90-3-251-271 (full-text access incomplete for this comparison).
