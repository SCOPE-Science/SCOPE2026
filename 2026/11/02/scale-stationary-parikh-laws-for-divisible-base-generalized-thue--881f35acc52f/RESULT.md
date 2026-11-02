# Scale-stationary Parikh laws for divisible-base generalized Thue–Morse words

## Finding

Fix integers \(B\ge 2\) and \(m\ge2\) with \(m\mid B\). Write \(s_B(j)\) for the base-\(B\) digit sum of an integer \(j\ge0\), and define the infinite word \(t(j)=s_B(j)\bmod m\) on \(\{0,\ldots,m-1\}\). For each integer \(e\ge0\), consider the factor of length \(L_e=B^{e+1}\) beginning at position \(i\). Its **centered Parikh vector** is

\[
 V_e(i)=\left(\#\{0\le h<L_e:t(i+h)=\ell\}-\frac{L_e}{m}\right)_{\ell=0}^{m-1}\in\mathbb Z^m.
\]

Define the cyclic-prefix count vector \(P_r(a)\in\{0,1\}^m\), for integers \(0\le r<m\) and residues \(a\in\mathbb Z/m\mathbb Z\), by

\[
 (P_r(a))_\ell=\sum_{h=0}^{r-1}\mathbf1_{\{(a+h)\bmod m=\ell\}}.
\]

For \(0\le c<m\) put

\[
 q_{B,m}(c)=\frac{(B-1)B^{m-c-1}}{B^m-1}.
\]

**Theorem.** For every \(v\in\mathbb Z^m\), the natural density of starting indices \(i\) satisfying \(V_e(i)=v\) exists and has the following value, **independent of \(e\)**:

\[
 \boxed{\mathbb P(V_e=v)=\frac{\mathbf1_{\{v=\mathbf0\}}}{m}
 +\frac1{m^2}\sum_{r=1}^{m-1}\sum_{a=0}^{m-1}\sum_{c=0}^{m-1}
 q_{B,m}(c)\,\mathbf1_{\{P_r(a+c+1)-P_r(a)=v\}}.}
\]

Every value is a rational number. The distribution is invariant under cyclic coordinate rotation and sign reversal, and every coordinate of \(V_e\) belongs to \(\{-1,0,1\}\). In particular, the probability that a length-\(L_e\) factor is *perfectly balanced*, meaning that it has exactly \(L_e/m\) occurrences of every letter, is

\[
 \boxed{\mathbb P(V_e=\mathbf0)=\frac1m+\frac{(m-1)(B-1)}{m(B^m-1)}.}
\]

The theorem gives the full distribution of **every additive letter-weight observable** at these lengths: for any fixed weights \(w_0,\ldots,w_{m-1}\), the centered weighted sum is \(\sum_\ell w_\ell (V_e(i))_\ell\), and its distribution follows by collecting vectors with equal scalar product. For example, at \(B=m=3\), assigning weights \((0,1,2)\) gives deviation probabilities \((4/39,8/39,5/13,8/39,4/39)\) at deviations \((-2,-1,0,1,2)\), for **every** \(e\ge0\). The six nonzero Parikh deviations each have probability \(4/39\).

## Assumptions and scope

The divisibility assumption \(m\mid B\) is essential to the proof: every length-\(B\) substitution block must contain each alphabet symbol equally often. The word starts at index zero and factors are contiguous, not cyclic. All limiting probabilities refer to natural density of starts, namely \(\lim_{N\to\infty}N^{-1}\#\{0\le i<N:V_e(i)=v\}\), for **fixed** \(e,B,m,v\); this is not a uniform-in-\(e\) convergence-rate claim. The centering \(L_e/m\) is integral. For \(m=2\), the same theorem applies.

## Proof

**1. Substitution blocks.** The identity

\[
 t(Bj+s)=(t(j)+s)\bmod m\qquad(0\le s<B)
\]

follows immediately from base-\(B\) digits. Because \(m\mid B\), the block of length \(B\) with index \(j\) contains each letter exactly \(B/m\) times. For any integer \(s=km+r\), \(0\le r<m\), the count vector in its first \(s\) places is \(k\mathbf1+P_r(t(j))\), where \(\mathbf1\) is the all-one vector.

Let \(N=B^e\), \(i=Bj+s\), and \(L_e=BN\). Comparing the length-\(BN\) factor beginning at \(Bj\) with the one beginning at \(Bj+s\) removes the initial \(s\) letters and adds the first \(s\) letters of the block indexed by \(j+N\). All \(N\) complete blocks contribute \(L_e/m\) of each symbol, hence the **exact, pointwise** identity

\[
 V_e(Bj+s)=P_{s\bmod m}(t(j+N))-P_{s\bmod m}(t(j)). \tag{1}
\]

Thus the entire deviation depends only on the residue of the within-block start and on the two endpoint letters, not on \(e\) through the number of complete blocks.

**2. Carry-length law.** Let \(C_e(j)\) be the number of consecutive base-\(B\) digits equal to \(B-1\) at positions \(e,e+1,\ldots\) of \(j\), stopping at the first digit smaller than \(B-1\). This number is finite for every \(j\ge0\). Adding \(B^e\) changes the digit sum by \(1-(B-1)C_e(j)\); consequently

\[
 t(j+B^e)\equiv t(j)+1+C_e(j)\pmod m. \tag{2}
\]

For each fixed \(c\ge0\), the condition \(C_e(j)=c\) constrains the \(c\) digits at positions \(e,\ldots,e+c-1\) to equal \(B-1\), and the next digit to be smaller. Its natural density is \((B-1)/B^{c+1}\). Conditional on these constraints, \(t(j)\) is uniformly distributed on \(\mathbb Z/m\mathbb Z\): one completely free base-\(B\) digit at position \(e+c+1\), above the constrained digits, takes each residue modulo \(m\) equally often since \(m\mid B\). This is exact over any aligned block of \(B^{e+c+2}\) consecutive integer inputs, even if higher digits contribute an arbitrary common shift. For fixed \(e,c\), incomplete endpoint blocks disappear as the observed interval grows. Therefore

\[
 \mathbb P(t(j)=a,\ C_e(j)=c)=\frac{B-1}{mB^{c+1}}. \tag{3}
\]

This implies an actual joint limiting law, not merely a statement along special subsequences: the tail condition \(C_e(j)\ge K\) is periodic modulo \(B^{e+K}\) and has density \(B^{-K}\), so the sum of the omitted carry cases tends to zero. Combining all \(c\equiv c_0\pmod m\) yields

\[
 \mathbb P(t(j)=a,\ C_e(j)\equiv c_0\bmod m)=\frac1m\sum_{h\ge0}\frac{B-1}{B^{c_0+hm+1}}=\frac{q_{B,m}(c_0)}m. \tag{4}
\]

In particular, this joint law is the same for every \(e\ge0\).

**3. Assemble the law.** As \(i\) ranges over consecutive nonnegative integers, \(s=i\bmod B\) is uniform on \(\{0,\ldots,B-1\}\). Because \(m\mid B\), \(r=s\bmod m\) is uniform on \(\{0,\ldots,m-1\}\). Substitute (2) into (1), and average using the joint law (4). The \(r=0\) term is always zero, while the \(r>0\) terms are precisely the stated finite sum. Each \(P_r(a)\) is a zero-one vector, so deviations have coordinates in \(\{-1,0,1\}\). Rationality follows from the explicit rational \(q_{B,m}\).

**4. Perfect balance and symmetries.** For any \(0<r<m\), the \(m\) vectors \(P_r(a)\) are distinct: each marks a proper consecutive circular interval with a unique initial boundary. Thus \(P_r(a+c+1)=P_r(a)\) exactly when \(c=m-1\). The \(r=0\) case contributes \(1/m\), and the other \(m-1\) choices of \(r\) together contribute \((m-1)q_{B,m}(m-1)/m\), establishing the displayed perfect-balance formula. Summing over a uniform starting letter \(a\) makes the law invariant under cyclic coordinate rotation. For sign symmetry, the complement of the interval of length \(r\) starting at \(a\) is the interval of length \(m-r\) starting at \(a+r\); passing from \(r\) to \(m-r\) changes the Parikh difference to its negative. These paired cases have the same weight. This completes the proof.

## Verification

The accompanying standalone `verify.py` computes the rational finite sum using `fractions.Fraction` and generates independent finite prefixes directly from the substitution, without digit-sum generation. It compares the formulas with sliding-window Parikh counts at multiple powers for bases and moduli \((2,2),(3,3),(4,4),(6,3),(4,2)\), checks the exact conditional carry/letter frequencies on representative finite blocks, and tests normalizations and both symmetries. On the supplied code, execution returned `VERIFY_OK checks= 199`, with the stated rational marginals. These finite comparisons test calculations and conventions; the proof of natural-density and exact all-exponent equality is above.

## Relationship to prior work

Chen and Wen (first public 2018-09-18) determine possible Parikh vectors and their *number* for generalized Thue–Morse factors. Popoli, Shallit and Stipulanti (first public 2024-10-03, Theorems 22–23) compute additive-complexity values and weight-dependent *numbers of classes*, including the ternary case. Neither result assigns probabilities to the different Parikh classes. Balková (first public 2011-07-25) develops factor-frequency methods and lists sets of frequencies of **individual full factors**; those algorithms in principle permit separately aggregating factors of a fixed length, but the inspected results do not state the finite closed law for Parikh-class masses or its exact invariance over every substitution exponent. Golafshan, Rigo and Whiteland (first public 2024-12-24, especially Sections 1–2 and 9) characterize binomial-equivalence classes and Abelian Rauzy graphs but count graph vertices and edges rather than natural-density masses of Parikh classes. The present assertion is therefore about a distribution over factors, not about the already-known complexity support or general existence of factor frequencies. The frequency method is deliberately elementary, using explicit block boundaries and geometric carries rather than a factor-frequency enumeration.

## Limitations

The theorem does not cover bases \(B\) that are not divisible by \(m\), lengths other than \(B^{e+1}\), or uniform convergence when \(e\) grows together with the sample cutoff. The result gives exact natural densities, not an assertion that finite prefixes contain the limiting proportions exactly. Established Parikh-support counts and individual-factor frequency methods are acknowledged as prior work. An equivalent Parikh-measure statement in unindexed or inaccessible literature remains possible; originality is based on the cited full-text comparison and recoverable search evidence, not inferred from search failure alone.

## References

1. P. Popoli, J. Shallit, M. Stipulanti, *Additive word complexity and Walnut*, first public 2024-10-03, arXiv:2410.02409, https://arxiv.org/abs/2410.02409 .
2. J. Chen, Z.-X. Wen, *On the abelian complexity of generalized Thue-Morse sequences*, first public 2018-09-18, arXiv:1809.06554, https://arxiv.org/abs/1809.06554 .
3. Ľ. Balková, *Factor frequencies in generalized Thue-Morse words*, first public 2011-07-25, arXiv:1107.5033, https://arxiv.org/abs/1107.5033 .
4. M. Golafshan, M. Rigo, M. Whiteland, *Computing the k-binomial complexity of generalized Thue-Morse words*, first public 2024-12-24, arXiv:2412.18425, https://arxiv.org/abs/2412.18425 .
