# Exact binary systematic linear function separation at distance four

## Finding

Let \(k,\ell\) be positive integers, let \(\mathcal E=(e_1,\ldots,e_k)\) be the fixed standard basis of \(\mathbb F_2^k\), and let \(f:\mathbb F_2^k\to\mathbb F_2^\ell\) be linear. Put
\[
\nu(f)=\big|\{f(e_i):1\le i\le k,\ f(e_i)\ne0\}\big|,
\]
where braces denote a set, so repeated nonzero images are counted once. Among all **linear systematic encoders** \(E_P(x)=(x,xP)\), with \(P\in\mathbb F_2^{k\times r}\), the minimum redundancy guaranteeing
\[
\min_{f(x)\ne0}\bigl(\operatorname{wt}(x)+\operatorname{wt}(xP)\bigr)\ge4
\]
is exactly
\[
\boxed{\ r_f^{\mathrm{sys,lin}}(4)=
\begin{cases}
0,&\nu(f)=0,\\
\min\{r\in\mathbb Z:r\ge3,\ \nu(f)\le2^{r-1}-r\},&\nu(f)\ge1.
\end{cases}\ }
\]
In particular, if the columns of \(f\) are all the nonzero elements of \(\mathbb F_2^s\) exactly once, then its optimal systematic redundancy at prescribed separation four is \(s+2\) for every \(s\ge1\).

## Assumptions and scope

All vector spaces, encoders, and Hamming weights are binary. The original \(k\) message coordinates are transmitted unmodified and the last \(r\) parity coordinates are linear combinations of them; their order is arbitrary. The protected value is \(f(x)\), not necessarily the whole message. The function \(f\) need not be surjective onto the chosen codomain, and its matrix may have repeated columns or zero columns. Since the encoding and function are linear, separating all pairs with different function values is equivalent to requiring the displayed minimum over nonzero differences \(x\) with \(f(x)\ne0\). The minimum over an empty set is taken to be infinite, covering the zero function.

## Proof

**Lower bound.** Let \(P\) achieve separation at least four. For each distinct nonzero vector \(a=f(e_i)\), select one index \(i\) representing \(a\), and denote the corresponding row of \(P\) by \(p_a\). The difference \(e_i\) has protected function value \(a\ne0\); hence \(1+\operatorname{wt}(p_a)\ge4\), so \(\operatorname{wt}(p_a)\ge3\). For distinct nonzero images \(a\ne b\), the difference \(e_i+e_j\) has protected value \(a+b\ne0\), because the field is binary. Thus
\[
2+\operatorname{wt}(p_a+p_b)\ge4,
\]
which says that all selected rows have pairwise Hamming distance at least two.

Fix one of the \(r\) parity positions and partition \(\mathbb F_2^r\) into the \(2^{r-1}\) adjacent pairs obtained by toggling that position. An independent set in the hypercube (a set with pairwise distance at least two) contributes at most one vector to each pair. For every prefix in \(\mathbb F_2^{r-1}\) of weight zero or one, **both** vectors in its pair have weight at most two. There are \(1+(r-1)=r\) such pairs, none of which can contain a selected row. Consequently
\[
\nu(f)\le2^{r-1}-r.
\]
If \(f\) is nonzero, one selected row exists, so \(r\ge3\), and the asserted lower bound follows.

**Construction.** Conversely, for every integer \(r\ge3\), let
\[
S_r=\{p\in\mathbb F_2^r:\operatorname{wt}(p)\ge3,\quad\operatorname{wt}(p)\equiv1\pmod2\}.
\]
The odd-weight vectors number \(2^{r-1}\), and the only odd-weight vectors of weight below three are the \(r\) unit vectors. Therefore \(|S_r|=2^{r-1}-r\). Suppose \(\nu(f)\le|S_r|\), and choose an injection \(\phi\) from the distinct nonzero values \(f(e_i)\) into \(S_r\). Set the \(i\)th row of \(P\) to \(\phi(f(e_i))\) when \(f(e_i)\ne0\) and to the zero vector otherwise.

For any \(x\) with \(f(x)\ne0\), if \(\operatorname{wt}(x)\ge4\), separation is automatic. For weight one, its parity row has weight at least three. For weight two, either the two nonzero images are unequal (and their distinct odd-weight parity rows differ in at least two coordinates), or exactly one input position has nonzero function image (and its parity row has weight at least three); the excluded remaining case has \(f(x)=0\). For weight three, the number of selected nonzero function images is one, two, or three. With one such image, the parity sum is an element of \(S_r\). With two, their function images must be different if \(f(x)\ne0\), so their parity vectors are different. With three, the XOR of three odd-weight parity vectors has odd weight and is nonzero. Thus \(\operatorname{wt}(xP)\ge4-\operatorname{wt}(x)\) in all cases. The encoder meets separation four, proving the sharp formula.

For the stated projective-complete example, \(\nu(f)=2^s-1\). At \(r=s+1\), the bound is \(2^s-(s+1)<2^s-1\); at \(r=s+2\), \(2^{s+1}-(s+2)\ge2^s-1\) for all \(s\ge1\). Hence the optimum is \(s+2\).

## Verification

Run `python3 verify.py` using standard Python. The standalone program exhaustively searches all parity matrices up to four redundancy coordinates for every \(f:\mathbb F_2^k\to\mathbb F_2^2\) with \(1\le k\le3\), totaling 84 functions, and agrees with the formula. It separately constructs and exhaustively checks all message differences for the projective-complete functions with \(s=1,2,3,4\), and checks the claimed cardinality and distance properties of \(S_r\) for \(3\le r\le8\). The program prints `VERIFY_OK`. These are finite cross-checks of the all-parameter mathematical proof, not substitutes for it.

## Relationship to prior work

Duy Ho, *On systematicity of linear function-correcting codes* (first public version 29 August 2026, arXiv:2608.29389v1), defines the systematic linear separation problem and exactly solves prescribed separations up to three. Its Theorem 5.6 counts non-coordinate projective points at separation three, and Remark 5.13 explicitly leaves separation four for future work. The present theorem gives the **entire binary distance-four answer**, including arbitrary zero and repeated function columns, by a sharp odd-weight hypercube matching argument; it does not claim any nonbinary formula.

When \(f\) is the identity, the statement reduces to the classical sharp binary systematic minimum-distance-four redundancy bound represented by extended Hamming codes. The new content is its uniform extension to protection of **any** binary linear function, where the relevant invariant is the number of distinct nonzero function-column images, not the message dimension or function rank. Earlier UEP work by Clark, Dunning, and Rogers addresses related distance-four parity-check problems, but no inspected source states this all-function exact formula.

## Limitations

The classification assumes binary linear functions and **linear systematic encoders** with a fixed distinguished input basis, and concerns prescribed separation four only. It does not determine the optimal redundancy for nonlinear encoders, nonbinary functions, or separations greater than four. The upper bound is constructive but does not classify all optimal parity matrices. The historical UEP literature creates a residual possibility that an equivalent general statement was obtained under another formulation; the 1990 Clark–Dunning–Rogers article was not fully accessible in this comparison. Independent validation has not been performed.

## References

1. D. Ho, *On systematicity of linear function-correcting codes*, arXiv:2608.29389v1 (29 August 2026), Sections 2, 4 and 5, especially Theorem 5.6 and Remark 5.13. https://arxiv.org/abs/2608.29389 ; open HTML: https://arxiv.org/html/2608.29389v1
2. W. E. Clark, L. A. Dunning, and D. G. Rogers, *Binary set functions and parity check matrices*, Discrete Mathematics 80 (1990), 249–265. Comparison based on bibliographic and abstract material, not full-text examination.
3. *Extended Hamming code*, Error Correction Zoo, https://errorcorrectionzoo.org/c/extended_hamming (accessed October 2026); classical \([2^m,2^m-m-1,4]\) family.
