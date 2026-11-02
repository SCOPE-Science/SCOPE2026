# Square-zero local ideal-product probabilities and a minimal field-recognition counterexample

## Finding

For a finite commutative ring \(R\) with identity, write \(\mathcal I(R)\) for its set of ideals and define, for every integer \(k\ge2\),
\[
\zeta_k(R)=\frac{\#\{(I_1,\ldots,I_k)\in\mathcal I(R)^k:I_1\cdots I_k=0\}}{|\mathcal I(R)|^k}.
\]
Let \(R\) be a nonfield finite local commutative ring with maximal ideal \(J\), \(J^2=0\), residue field \(F=R/J\) of order \(q\), and \(d=\dim_F J\ge1\). Define the Gaussian-subspace count
\[
S(q,d)=\sum_{j=0}^{d}{d\brack j}_q,
\qquad
{d\brack j}_q=\prod_{i=0}^{j-1}\frac{q^{d-i}-1}{q^{j-i}-1}.
\]
Here \(S(q,d)\) counts the \(F\)-linear subspaces of \(J\), including zero and \(J\).

**Theorem.** For every such \(R\) and every integer \(k\ge2\),
\[
\boxed{\zeta_k(R)=1-\frac{1+k(S(q,d)-1)}{(S(q,d)+1)^k}.}
\]
In particular the sequence depends only on \((q,d)\), and not on the characteristic or the extension class of the local ring.

For any finite field \(F'\), \(\zeta_k(F')=1-2^{-k}\). Within the above nonfield square-zero local family, equality with this field value occurs **if and only if**
\[
\boxed{(q,d,k)=(2,2,2).}
\]
The comparison is sharp: when \(d=1\), the local value is *smaller* than the field value for \(k=2,3\) and *larger* for all \(k\ge4\); when \(d\ge2\), it is *larger* for all \(k\ge2\) except the unique equality case.

An explicit equality example is the eight-element ring
\[
A=\mathbb F_2[x,y]/(x^2,xy,y^2).
\]
It has exactly six ideals, and exactly 27 of the 36 ordered pairs of ideals have product zero. Consequently
\[
\boxed{\zeta_2(A)=27/36=3/4=\zeta_2(\mathbb F_2),}
\]
even though \(A\) is not a field. This disproves the unrestricted field-recognition assertion in Conjecture 4.2 of Chakraborty and Patra's 2026 *Ideal Zero-Product Probability in Finite Commutative Rings*. The ring \(A\) is a smallest-cardinality nonfield counterexample: no commutative unital nonfield with fewer than eight elements has \(\zeta_2=3/4\).

## Assumptions and scope

All rings in the theorem are finite, nonzero, commutative, associative and unital. The main formula concerns local rings with \(J^2=0\) and \(J\ne0\); no splitting of \(R\to R/J\) is assumed. The Gaussian parameters satisfy \(q\ge2\) a prime power and \(d\ge1\). The number \(k\) of independently sampled, uniformly random ideals is any integer at least two. The equality comparison uses the *ideal-product* invariant, not the different probability of a product of randomly sampled **elements** being zero. The field case has \(d=0\) and is treated separately.

## Proof

**Step 1: Determine all proper ideals.** Every proper ideal of a local ring is contained in its maximal ideal \(J\). Because \(J^2=0\), the action of \(R\) on the additive group of \(J\) factors through \(R/J=F\): if two representatives differ by \(j\in J\), their actions differ by multiplication by \(j\), which annihilates \(J\). Thus \(J\) is an \(F\)-vector space. An additive subgroup \(I\subseteq J\) is an ideal precisely when it is an \(F\)-linear subspace. There are therefore exactly \(S(q,d)\) proper ideals, counting \(0\) and \(J\), and exactly one additional ideal, \(R\).

**Step 2: Count all nonzero ideal products.** The product of two proper ideals is zero because both lie in \(J\). Multiplication by \(R\) leaves each ideal unchanged. Hence the product of an ordered \(k\)-tuple of ideals is nonzero precisely when all \(k\) choices are \(R\), or exactly one choice is a nonzero proper ideal while all others are \(R\). The two cases give respectively \(1\) and \(k(S(q,d)-1)\) tuples. Division by \((S(q,d)+1)^k\) proves the displayed probability formula. This also proves extension-class independence, including rings of different characteristics.

**Step 3: Establish the field comparison and all equality cases.** A field has two ideals, giving \(1-2^{-k}\). For \(d=1\), the only proper ideals are \(0,J\), so \(S=2\) and
\[
\zeta_k(R)=1-\frac{k+1}{3^k}.
\]
Equality with a field would require \(2^k(k+1)=3^k\), impossible for positive \(k\) by parity. The ratio of the nonzero-product probabilities is \((k+1)(2/3)^k\); it exceeds one for \(k=2,3\), is less than one for \(k=4\), and is strictly decreasing thereafter because the ratio at consecutive \(k\)'s is \(2(k+2)/(3(k+1))<1\) for \(k\ge2\). This proves the assertions for \(d=1\).

For \(d\ge2\), the number of subspaces is at least five. Equality \(S=5\) occurs exactly when \((q,d)=(2,2)\): at \(d=2\), \(S=q+3\); at \(d\ge3\), the zero subspace, the whole space and at least seven one-dimensional subspaces already give \(S>5\). For \(k=2\) the difference from the field probability is exactly
\[
\zeta_2(R)-\frac34=\frac{(S-1)(S-5)}{4(S+1)^2}.
\]
It vanishes exactly at \(S=5\) and is positive for larger \(S\). For \(k\ge3\), put \(t=(S+1)/2\ge3\). The inequality \(\zeta_k(R)>1-2^{-k}\) is equivalent to
\[
t^k>1+2k(t-1).
\]
At \(t=3\) this holds for all \(k\ge3\) because \(3^k>4k+1\) (base case \(k=3\) and induction). For fixed \(k\ge3\), the difference between the two sides increases on \([3,\infty)\), since its derivative is \(kt^{k-1}-2k>0\). This proves the full comparison and equality classification.

**Step 4: Exhibit and minimize the counterexample.** In \(A\), the maximal ideal \(J=(x,y)\) satisfies \(J^2=0\), the residue field is \(\mathbb F_2\), and \(J\) has dimension two. Its proper ideals are \(0,(x),(y),(x+y),J\); adding \(A\) gives six ideals. Among 36 pairs, nine have nonzero products: \((A,A)\) and the eight ordered pairs with exactly one nonzero proper ideal and the other \(A\). Thus the other 27 pairs give zero, proving the explicit equality.

For the minimality claim, every commutative unital nonfield of cardinality less than eight has cardinality four or six. The order-four possibilities are \(\mathbb Z/4\mathbb Z\), \(\mathbb F_2[t]/(t^2)\), and \(\mathbb F_2\times\mathbb F_2\) (apart from the field \(\mathbb F_4\)); the order-six possibility is \(\mathbb Z/6\mathbb Z\). A length-two chain ring has \(\zeta_2=2/3\), while a product of two fields has \(\zeta_2=(3/4)^2=9/16\). Neither equals \(3/4\), establishing minimality. This does not claim to classify all order-eight rings attaining equality.

## Verification

The standalone program `verify.py` constructs the multiplication tables of both \(\mathbb F_2[x,y]/(x,y)^2\) and the nonsplit-characteristic companion \((\mathbb Z/4\mathbb Z)[t]/(2t,t^2)\). It enumerates every additive subgroup, filters for multiplicative closure, and checks every ordered tuple of ideals for \(2\le k\le5\) using actual ring multiplication. Both rings have exactly six ideals with cardinalities \(1,2,2,2,4,8\), and yield respectively 27, 203, 1279 and 7755 zero-producing tuples at lengths two through five. The script also checks representative finite-field Gaussian counts and the predicted comparison sign for \(2\le k<15\); it ends with `VERIFY_OK`. A second standalone program, `verify_small.py`, independently enumerates ideals and ordered zero-product pairs of the four nonfield rings of cardinality below eight; all four independent checks agree with the minimality argument.

Run from the directory containing the files using `python3 verify.py` and `python3 verify_small.py`. Exact expected outputs are included in `verification_output.txt` and `verification_small_output.txt`. The all-field/all-length theorem is proved symbolically above; these finite computations only corroborate it.

## Relationship to prior work

Chakraborty and Patra, *Ideal Zero-Product Probability in Finite Commutative Rings* (arXiv:2608.14618, 2026), introduce \(\zeta_k\), compute it for fields, finite Boolean rings, chain rings, and finite principal ideal rings, and formulate Conjecture 4.2 asserting that the field value characterizes finite fields. Their Section 10 explicitly asks for formulas beyond chain rings and for dependence on other ring invariants. Those definitions, the field benchmark and the chain-ring calculations are established prior results. The present result supplies a complete nonprincipal short-local family and a smallest-order counterexample to the field-characterization conjecture.

Earlier literature on the zero-product probability of **ring elements** (for example, Esmkhani and Jafarian Amiri, 2018) concerns a different sample space and cannot imply the ideal-product formula by identifying the two probabilities. The subspace-counting ingredients are classical; neither the Gaussian coefficients nor the elementary classification of square-zero ideals is claimed as new in isolation.

## Limitations

The proof does not classify \(\zeta_k\) for general local rings with nonzero \(J^2\), nor does it classify all finite commutative rings having the same ideal-zero-product probability as a field. In particular, the absence of a square-zero local counterexample at \(k\ge3\) does not imply that the field-recognition assertion holds for all rings at those lengths. Equality at \(k=2\) among square-zero local rings is fully resolved, but global uniqueness or priority beyond the inspected literature has not been independently established.

## References

1. S. Chakraborty and S. K. Patra, *Ideal Zero-Product Probability in Finite Commutative Rings*, arXiv:2608.14618 (first arXiv version August 13, 2026; inspected subsequent full-text version), Sections 2–4, 7, and 10, especially Conjecture 4.2. https://arxiv.org/abs/2608.14618
2. M. A. Esmkhani and S. M. Jafarian Amiri, *The probability that the multiplication of two ring elements is zero*, Journal of Algebra and Its Applications **17** (2018), 1850054. https://doi.org/10.1142/S0219498818500540
3. Standard finite linear algebra: the number of \(j\)-dimensional subspaces of \(\mathbb F_q^d\) is the Gaussian binomial coefficient \({d\brack j}_q\).
