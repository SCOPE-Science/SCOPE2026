# A conditional Poisson regularity law for partition-surjective transformation semigroups

## Finding

Let \(\mathcal P_0\) be a nonempty finite partition into labeled nonempty blocks, let \(b\) be an integer strictly larger than the size of every block of \(\mathcal P_0\), and adjoin \(M\ge1\) labeled blocks of size \(b\). Write \(\mathcal P_M\) for the resulting partition. Let \(\Gamma(\mathcal P_M)\) denote the monoid of maps that take each domain block **onto** some target block (not merely into one), and choose \(F_M\) uniformly from this finite monoid.

For each lower block \(B\in\mathcal P_0\), define
\[
 w_B=|B|!\,S(b,|B|),\qquad d=b!,\qquad C=\sum_{B\in\mathcal P_0}w_B,
\]
where \(S(\cdot,\cdot)\) is a Stirling number of the second kind. Let \(F_0\) be the restriction of \(F_M\) to the union of lower blocks, and let \(N_B\) count size-\(b\) source blocks that map onto \(B\). Then \(F_0\) is uniform on \(\Gamma(\mathcal P_0)\), independent of the vector \(N=(N_B)\), and \(N\) has the exact marked-multinomial law
\[
 (N_B:B\in\mathcal P_0,\;M-\sum_BN_B)
 \sim\operatorname{Multinomial}
 \left(M;\left(\frac{w_B}{Md+C}\right)_{B\in\mathcal P_0},\frac{Md}{Md+C}\right).
\]
In total variation, jointly with \(F_0\), this law is within
\[
 \boxed{\frac{2C^2}{Md^2}}
\]
of the law in which \(F_0\) retains its uniform distribution and the \(N_B\) are mutually independent \(\operatorname{Poisson}(w_B/d)\) variables. A bound larger than one is understood as vacuous.

Define the lower **witness set** \(W(f_0)\) to consist of blocks \(B\in\mathcal P_0\) for which some source block \(A\in\mathcal P_0\) of the same size maps onto \(B\) under \(f_0\); let \(L(f_0)=\mathcal P_0\setminus W(f_0)\). A map is von Neumann regular if it has a generalized inverse \(g\) satisfying \(fgf=f\). The exact and limiting regular proportions are
\[
 \boxed{
 R_M=\mathbb E_{F_0}\left[
 \mathbf1_{\{F_0\text{ regular}\}}
 \left(1-\frac{\sum_{B\in L(F_0)}w_B}{Md+C}\right)^M
 \right],}
\]
\[
 \boxed{
 R_\infty=\mathbb E_{F_0}\left[
 \mathbf1_{\{F_0\text{ regular}\}}
 \exp\left(-\frac{\sum_{B\in L(F_0)}w_B}{d}\right)
 \right],\qquad |R_M-R_\infty|\le\frac{2C^2}{Md^2}.}
\]
Here \(R_\infty>0\). More strongly, conditional on \(F_M\) being regular, the joint law of the background map \(F_0\) and the entire lower-target vector \(N\) converges in total variation to the following explicit tilted law: \(f_0\) has mass proportional to
\[
 \mathbf1_{\{f_0\text{ regular}\}}\exp\left(-\sum_{B\in L(f_0)}w_B/d\right);
\]
given \(f_0\), all \(N_B\) with \(B\in L(f_0)\) are zero, while all \(N_B\) with \(B\in W(f_0)\) are independent Poisson variables of means \(w_B/d\). The conditional total-variation distance is at most \(4C^2/(Md^2R_\infty)\).

This law describes the full finite-background regularity profile, including intrinsic defects of \(f_0\), rather than only an unconditioned cardinality.

## Assumptions and scope

The blocks are distinct and labeled, with arbitrary finite positive lower block sizes strictly less than \(b\); \(M\to\infty\) while \(\mathcal P_0\) and \(b\) remain fixed. All maps are uniformly sampled among the **surjective-on-each-block** transformations. These are not the larger monoid of maps that send each block merely *into* one block. Multiplication is ordinary function composition. No algebraic closure beyond the finite transformation monoid is assumed. The image of a map is a union of entire target blocks. All inequalities and convergence statements hold for every \(M\ge1\), apart from limiting assertions as \(M\to\infty\).

## Proof

**1. The regularity witness criterion.** For any finite partition \(\mathcal P\) and any \(f\in\Gamma(\mathcal P)\), regularity is equivalent to the following: each target block \(B\) in the image of \(f\) has a source block \(A\) with \(|A|=|B|\) and \(f(A)=B\). Indeed, equality of sizes makes the surjective restriction \(f|_A\) bijective. Choosing one inverse bijection \(B\to A\) for each image block and mapping every other block surjectively onto a block of minimum size constructs \(g\in\Gamma(\mathcal P)\) with \(fgf=f\). Conversely, if \(fgf=f\) and \(B\) is an image block, then \(f\circ g\) restricts to the identity on \(B\). Since \(g\) maps \(B\) onto some block \(A\), it follows that \(f(A)=B\) and both surjections \(B\to A\to B\) have equal finite cardinalities. Thus \(f|_A\) is bijective and \(|A|=|B|\). This is the finite form of the criterion in Sarkar--Singh, Theorem 5.5.

**2. Exact decomposition and finite law.** No lower block can surject onto a size-\(b\) target. Therefore its restriction defines \(F_0\in\Gamma(\mathcal P_0)\). Each upper source block independently has \(d=b!\) bijections to any one of the \(M\) upper targets, and exactly \(w_B=|B|!S(b,|B|)\) surjections to a lower target \(B\). Hence it has \(Md+C\) equally counted choices, independently of lower choices. Uniformity yields the asserted product decomposition and multinomial law.

**3. Quantitative independent-Poisson limit.** Let \(K=\sum_BN_B\), and set \(p=C/(Md+C)\). Then \(K\sim\operatorname{Binomial}(M,p)\), and conditional on \(K\), target marks are independent with probabilities \(w_B/C\). Couple each Bernoulli trial of parameter \(p\) to an independent \(\operatorname{Poisson}(p)\) variable: their total-variation distance is \(p(1-e^{-p})\le p^2\). Product coupling and summation give \(d_{\rm TV}(K,\operatorname{Poisson}(Mp))\le Mp^2\). Since \(Mp\le C/d\), adding an independent Poisson increment shows \(d_{\rm TV}(\operatorname{Poisson}(Mp),\operatorname{Poisson}(C/d))\le C/d-Mp\). Consequently the marked counts, and their joint law with the independent \(F_0\), are within
\[
 Mp^2+(C/d-Mp)
 =\frac{MC^2}{(Md+C)^2}+\frac{C^2}{d(Md+C)}
 \le\frac{2C^2}{Md^2}
\]
of the independent-Poisson limit. Independent Poisson marking yields each mean \(w_B/d\).

**4. Regularity and conditioning.** In the upper size class, every target block that is hit has a same-size bijective upper source, so it is automatically witnessed. For lower blocks, upper sources cannot provide equal-size witnesses. Thus \(F_M\) is regular precisely when \(F_0\) is regular and no upper source hits any \(B\in L(F_0)\). Conditional on \(F_0=f_0\), each upper source avoids these blocks with probability \(1-(\sum_{B\in L(f_0)}w_B)/(Md+C)\). Taking its \(M\)-th power proves the exact formula for \(R_M\). In the independent-Poisson law the corresponding avoidance probability is the displayed exponential, establishing the limit and error bound. The identity background map proves \(R_\infty>0\), because it is regular and witnesses every lower target. Conditioning the limiting independent-Poisson product law on the regularity event gives the explicitly tilted \(F_0\) distribution, forced zeros on \(L(f_0)\), and independent unmodified Poisson variables on \(W(f_0)\). For an event \(E\) of probability \(R_\infty>0\) under the limit law, total-variation error \(\varepsilon\) before conditioning entails error at most \(2\varepsilon/R_\infty\) after conditioning; substituting the preceding bound finishes the proof.

**5. A mixed-size example.** Take \(\mathcal P_0\) with three blocks of sizes \(1,1,2\) and let \(b=3\). The lower monoid has \(16\) maps. Four are regular with all three lower targets witnessed; four are regular with only the size-\(2\) block unwitnessed; four are regular with one singleton unwitnessed; two are regular with one singleton and the size-\(2\) block unwitnessed; the remaining two are irregular. The corresponding weights are \(1,1,6\), and \(d=6\). Hence
\[
 R_M=\frac{4+4(1-6/(6M+8))^M+4(1-1/(6M+8))^M+2(1-7/(6M+8))^M}{16},
\]
\[
 R_\infty=\frac{4+4e^{-1}+4e^{-1/6}+2e^{-7/6}}{16}
 \approx0.5925156945048388.
\]
This example has both intrinsic lower regularity failures and additional Poisson-induced failures. The finite probabilities at \(M=1\) and \(M=2\) are \(11/16\) and \(2083/3200\), respectively.

## Verification

The standalone program `check.py` enumerates every surjective-on-block map for nine finite block profiles, tests regularity using source-target witnesses, and independently searches for a generalized inverse for four small profiles. It verifies the exact regular count against independently aggregated weighted background choices. Two profiles additionally check every component of the full multinomial target-count vector, and three background profiles check the stated quantitative probability bound over twelve choices of \(M\). The run output is included as `check_output.txt`.

The direct checks cover \(19{,}954\) maps in the nine enumerated profiles. They are finite consistency checks, not a proof of the infinite-family theorem or of convergence.

## Relationship to prior work

Sarkar and Singh (arXiv:2010.14033, Theorem 5.5 and Section 6) prove the equal-size block-witness regularity criterion and give exact total cardinalities of regular elements for **arbitrary finite** partitions. Accordingly, neither that criterion nor the mere existence of a finite regularity-count formula is claimed new here. The contribution assessed here is the *joint marked Poisson limit with an explicit total-variation rate and the fully conditioned regular-element law* in the growing maximal-block regime, including multiple interacting lower sizes. The scalar expression for \(R_M\) is included to connect this new limiting statement to the established finite theory.

Dolinka and East (arXiv:1407.3312) study idempotent generation in the larger monoid of partition-preserving maps, with block images allowed to be proper subsets; that is a different counting problem. Some two-size boundary cases reproduce occupancy laws also encountered for equivariant maps of finite group sets; these are not presented as independently novel special cases. The mixed-size surjective-block transitions and their conditioned witness-defect mixture are the distinctive regime here.

## Limitations

The background partition and the maximal block size are fixed; no limit is claimed when lower-block multiplicities or \(b\) grow with \(M\). The quantitative bound may be vacuous for small \(M\). The theorem does not determine the asymptotic size of the entire semigroup without fixing the background. Primary-literature comparisons cannot exclude an equivalent unindexed formulation, and independent priority assessment remains outstanding. No independent audit has been performed.

## References

1. M. Sarkar and S. N. Singh, *Regular, Unit-Regular, and Idempotent Elements of Semigroups of Transformations That Preserve a Partition*, arXiv:2010.14033, initial public version 27 October 2020. https://arxiv.org/pdf/2010.14033 . Relevant: Theorem 5.5, Theorems 6.4 and 6.10.
2. I. Dolinka and J. East, *Idempotent Generation in the Endomorphism Monoid of a Uniform Partition*, arXiv:1407.3312, first public version 11 July 2014. https://arxiv.org/pdf/1407.3312 . Relevant: Introduction, Section 3.
