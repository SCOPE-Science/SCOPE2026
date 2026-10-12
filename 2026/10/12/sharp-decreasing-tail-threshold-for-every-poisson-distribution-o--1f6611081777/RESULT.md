# Sharp decreasing-tail threshold for every Poisson distribution of order \(k\)

## Finding

For each integer \(k\ge 2\), take independent \(N_1,\ldots,N_k\sim\operatorname{Poisson}(\lambda)\) with common \(\lambda>0\), and set \(X_{k,\lambda}=\sum_{j=1}^{k}jN_j\). Define
\[
S_k(\lambda)=\sum_{j=0}^{k}\binom{k}{j}\frac{\lambda^j}{(j+2)!},
\]
and let \(\lambda_k^\star\) be its unique positive solution of \(S_k(\lambda_k^\star)=1\). Then
\[
\boxed{\Pr(X_{k,\lambda}=n+1)<\Pr(X_{k,\lambda}=n)\quad\text{for every integer }n\ge k}
\]
holds **if and only if** \(0<\lambda<\lambda_k^\star\). The first obstruction at the endpoint is exact:
\[
\Pr(X_{k,\lambda_k^\star}=k+2)=\Pr(X_{k,\lambda_k^\star}=k+1).
\]
In particular, the sharp boundary is exactly the first neighboring tail crossing, proving the all-order threshold proposed as Conjecture 4.3 by Mane (2023). For \(k=2\), \(\lambda_2^\star=2(\sqrt7-2)\); for \(k=3\), \(\lambda_3^\star\) is the unique positive root of \(S_3(\lambda)=1\).

## Assumptions and scope

The integer \(k\) is finite and at least two, \(\lambda\) is strictly positive, all Poisson variables are mutually independent, and every component has the **same** mean \(\lambda\). The inequalities concern consecutive masses starting at index \(k\), not the global mode, and make no assertion about unequal component rates or other compound-Poisson jump laws.

Let \(p_n=p_n^{(k)}(\lambda)=e^{k\lambda}\Pr(X_{k,\lambda}=n)\). The common positive factor does not change mass comparisons, and
\[
P_k(z)=\sum_{n\ge0}p_nz^n=\exp\!\left(\lambda\sum_{j=1}^{k}z^j\right).
\]
We set \(p_n=0\) for negative integers \(n\), and \(p_0=1\). For all nonnegative \(n\), \(p_n>0\).

## Proof

**1. Initial coefficient identities.** Introduce the untruncated generating function
\[
Q(z)=\exp\!\left(\frac{\lambda z}{1-z}\right)=\sum_{n\ge0}q_nz^n.
\]
For \(n\ge1\), elementary series multiplication gives
\[
q_n=\lambda\sum_{i=0}^{n-1}\binom{n-1}{i}\frac{\lambda^i}{(i+1)!},\qquad
q_n-q_{n-1}=\lambda^2S_{n-2}(\lambda)\quad(n\ge2),
\]
with \(q_0=1\). For each integer \(t\ge0\), put
\[
T_t(\lambda)=\sum_{i=0}^{t}\binom{t}{i}\frac{\lambda^i}{(i+1)!};\qquad q_{t+1}=\lambda T_t(\lambda).
\]
The factorization
\[
P_k(z)=Q(z)\exp\!\left(-\frac{\lambda z^{k+1}}{1-z}\right)
\]
shows that, for \(k+1\le n\le2k+1\), the second exponential contributes only its constant and linear terms. Hence
\[
p_n=q_n-\lambda\sum_{a=0}^{n-k-1}q_a,\qquad p_n=q_n\ (0\le n\le k).
\]
Taking consecutive differences yields
\[
p_{k+1}-p_k=\lambda^2S_{k-1}(\lambda)-\lambda,\qquad
p_{k+2}-p_{k+1}=\lambda^2(S_k(\lambda)-1),
\]
and, for every integer \(0\le t\le k-2\),
\[
p_{k+2+t}-p_{k+1+t}=\lambda^2\bigl(S_{k+t}(\lambda)-T_t(\lambda)\bigr).
\]

**2. A factorial-convolution domination.** Vandermonde's identity gives, for every integer \(t\ge0\),
\[
S_{k+t}(\lambda)=\sum_{i=0}^{t}\binom ti\lambda^i
 \sum_{j=0}^{k}\binom kj\frac{\lambda^j}{(i+j+2)!}.
\]
For all integers \(i,j\ge0\),
\[
\frac1{(i+j+2)!}\le\frac1{(i+1)!(j+2)!},
\]
with strict inequality for \(i\ge1\). Indeed, the quotient \((i+j+2)!/(j+2)!\) is a product of \(i\) terms, each strictly larger than the corresponding factor in \((i+1)!\) when \(i\ge1\). Consequently
\[
S_{k+t}(\lambda)\le S_k(\lambda)T_t(\lambda),
\]
strictly for \(t\ge1\) and \(\lambda>0\). Since \(S_k(0)=1/2\), all its nonconstant coefficients are strictly positive, and it diverges as \(\lambda\to\infty\), the equation \(S_k(\lambda)=1\) has exactly one positive root \(\lambda_k^\star\). Whenever \(0<\lambda<\lambda_k^\star\), we have \(S_k(\lambda)<1\), so
\[
S_{k+t}(\lambda)-T_t(\lambda)
\le (S_k(\lambda)-1)T_t(\lambda)<0.
\]
Thus \(p_{k+1}>p_{k+2}>\cdots>p_{2k}\) in the entire proposed range.

**3. The first edge, including the exceptional second order.** For \(k\ge3\),
\[
S_k(1)\ge S_3(1)=\frac{17}{15}>1,
\]
so \(\lambda_k^\star<1\). Because \(S_{k-1}(\lambda)<S_k(\lambda)\) for every \(\lambda>0\), throughout \(0<\lambda\le\lambda_k^\star\) we have
\[
\lambda S_{k-1}(\lambda)
\le\lambda_k^\star S_{k-1}(\lambda_k^\star)
<\lambda_k^\star S_k(\lambda_k^\star)
=\lambda_k^\star<1.
\]
For \(k=2\), the unique positive root is \(r=2(\sqrt7-2)>6/5\). From \(S_2(r)=1\) we obtain \(r^2+8r=12\) and therefore
\[
rS_1(r)=\frac r2+\frac{r^2}{6}=2-\frac{5r}{6}<1.
\]
The function \(\lambda S_1(\lambda)\) is strictly increasing, so the same inequality holds for \(0<\lambda\le r\). The initial difference formula now gives \(p_k>p_{k+1}\) for all orders and all \(0<\lambda\le\lambda_k^\star\). Together with step 2, this establishes the strictly decreasing starting block \(p_k>p_{k+1}>\cdots>p_{2k}\) for every \(0<\lambda<\lambda_k^\star\).

**4. Propagation to every later index.** Differentiating \(P_k(z)\) gives the classical coefficient recurrence
\[
np_n=\lambda\sum_{j=1}^{k}jp_{n-j}\qquad(n\ge1).
\]
If for some \(n\ge2k\) the block \(p_{n-k}>p_{n-k+1}>\cdots>p_n\) is strictly decreasing, subtract the recurrences for consecutive indices:
\[
(n+1)p_{n+1}-np_n
=\lambda\sum_{j=1}^{k}j(p_{n+1-j}-p_{n-j})<0.
\]
Since \(p_n>0\), it follows that \(p_{n+1}<np_n/(n+1)<p_n\). Induction from the established starting block proves strict decrease for every \(n\ge k\).

**5. Sharpness and the endpoint.** Conversely, if \(\lambda\ge\lambda_k^\star\), the exact difference identity in step 1 gives \(p_{k+2}-p_{k+1}=\lambda^2(S_k(\lambda)-1)\ge0\). Strict decrease already fails at this single pair. At equality the two masses tie; above the threshold their order reverses. This completes the equivalence.

## Verification

A standalone standard-library checker (`verify.py`) uses exact rational polynomial arithmetic to independently regenerate the finite coefficient recurrence, the one-block convolution formula, the consecutive-difference formulas, and coefficientwise factorial domination for orders \(2\le k\le17\). It also checks rational samples of the mass sequence through index \(6k\), and exact rational bracketing for the exceptional second-order root. Run `python3 verify.py` alongside this file. The checker reports 504 successful bounded checks. These checks are finite corroboration; the proof above establishes the theorem for all orders, all admissible rates, and the full infinite tail.

## Relationship to prior work

Mane (2023b, arXiv:2310.05671v1), §4, states the precise decreasing-tail threshold as **Conjecture 4.3**, gives the first-block coefficient formulas, and supports the claimed threshold numerically; it does not prove the uniform all-order criterion. Mane (2023a, arXiv:2310.00827v1), Proposition 4.1, establishes the induction mechanism assuming a decreasing starting block and proves only a smaller sufficient range. The present result proves that the conjectured single crossing is sufficient for the entire block for every order, using factorial-convolution domination, and then applies the known propagation mechanism. Kwon–Philippou (2023) treats mode classifications for orders three and four, which are different from a sharp all-order monotone-tail criterion.

## Limitations

The order \(k\) is any finite integer at least two; the result does not extend by assertion to variable component Poisson rates, arbitrary jump weights, or a global-mode classification. The proof's analytic inequalities require \(\lambda>0\); at the boundary \(\lambda_k^\star\), strict decrease fails. The comparison with available literature cannot exclude an equivalent proof published under a different formulation.

## References

1. S. R. Mane, *Convexity and monotonicity of the probability mass function of the Poisson distribution of order k*, arXiv:2310.05671v1, first publicly posted 2023-10-09. See §4, Definition 4.2 and Conjecture 4.3. https://arxiv.org/html/2310.05671v1
2. S. R. Mane, *Analytical proofs for the properties of the probability mass function of the Poisson distribution of order k*, arXiv:2310.00827v1, first publicly posted 2023-10-02. See §4, Proposition 4.1 and Remark 4.4. https://arxiv.org/html/2310.00827v1
3. Y. Kwon and A. N. Philippou, *The Modes of the Poisson Distribution of Order 3 and 4*, Entropy 25 (2023), 699. https://doi.org/10.3390/e25040699
