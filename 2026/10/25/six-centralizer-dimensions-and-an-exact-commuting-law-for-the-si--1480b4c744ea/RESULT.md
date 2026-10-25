# Six centralizer dimensions and an exact commuting law for the six-generator exterior algebra

## Finding

Let \(q\) be an odd prime power, let \(V\) be a six-dimensional vector space over \(\mathbb F_q\), and let \(E=\bigwedge_{\mathbb F_q}V\). For any \(a\in E\), define its element-centralizer by \(C_E(a)=\{b\in E:ab=ba\}\), an \(\mathbb F_q\)-linear subspace of \(E\). The dimension of \(E\) is \(64\). Exactly six centralizer dimensions occur:

\[
\{\dim_{\mathbb F_q}C_E(a):a\in E\}=\{48,57,58,60,63,64\}.
\]

For Gaussian binomial coefficients \({n\brack k}_q=\prod_{i=0}^{k-1}(q^{n-i}-1)/(q^{k-i}-1)\), define

\[
D_3=(q-1){6\brack3}_q,\qquad
D_1={6\brack1}_q\left(q^{10}-1-(q-1){5\brack2}_q\right),\qquad
D_0=q^{20}-1-D_1-D_3.
\]

The number \(N_d\) of elements \(a\in E\) with \(\dim C_E(a)=d\) is as follows. Every entry in the second column is multiplied by \(q^{32}\), to account for arbitrary even components of \(a\).

| \(d\) | \(N_d/q^{32}\) |
| ---: | ---: |
| \(48\) | \((q^6-1)q^{26}\) |
| \(57\) | \(q^6D_0\) |
| \(58\) | \(q^6D_1\) |
| \(60\) | \(q^6D_3\) |
| \(63\) | \(q^6-1\) |
| \(64\) | \(1\) |

Consequently, for independently and uniformly sampled \(a,b\in E\),

\[
\boxed{\Pr(ab=ba)=\frac{q^{20}+q^{17}+q^{16}-q^{11}-q^{10}+q-1}{q^{33}}.}
\]

In particular, with dimension six fixed, this probability is \(q^{-13}(1+O(q^{-3}))\) as the odd prime power \(q\) grows.

## Assumptions and scope

The algebra is the **associative, unital** exterior algebra on a six-dimensional vector space; its elements are all (possibly inhomogeneous) exterior tensors. The coefficient field is any finite field of **odd** characteristic, not necessarily a prime field. An element-centralizer is not a maximal commutative subalgebra, and the claimed distribution is over uniformly sampled algebra elements, not over units or isomorphism classes. The Gaussian coefficients count linear subspaces over \(\mathbb F_q\). No assumption is made about invertibility of \(a\).

## Proof

**1. Reduction to an odd wedge-annihilator.** Write \(E=E_{\mathrm{even}}\oplus E_{\mathrm{odd}}\). Each summand has dimension \(32\), and the even summand lies in the center. Graded commutativity gives, for \(a,b\in E\),

\[
ab-ba=2a_{\mathrm{odd}}\wedge b_{\mathrm{odd}}.\]

Since the characteristic is odd, if \(u=a_{\mathrm{odd}}\) and \(K(u)=\{w\in E_{\mathrm{odd}}:u\wedge w=0\}\), then

\[\dim C_E(a)=32+\dim K(u).\]

Thus the problem reduces to one linear map on the \(32\)-dimensional odd part for every odd element \(u\).

**2. A nonzero degree-one part.** Write uniquely

\[u=v+\alpha+\gamma,\qquad v\in V,\ \alpha\in\bigwedge^3V,\ \gamma\in\bigwedge^5V.\]

Suppose \(v\ne0\). Choose a direct sum \(V=\langle v\rangle\oplus W\), where \(\dim W=5\), and write an arbitrary odd element as \(w+\beta+\delta\) in degrees \(1,3,5\). The degree-two equation \(v\wedge w=0\) forces \(w=\lambda v\), leaving one scalar. The degree-four equation \(v\wedge\beta+\alpha\wedge w=0\) uniquely determines the \(\bigwedge^3W\)-component of \(\beta\), leaving freely the \(v\wedge\bigwedge^2W\)-component of dimension \(10\). Finally the degree-six equation

\[v\wedge\delta+\alpha\wedge\beta+\gamma\wedge w=0\]

uniquely determines the \(\bigwedge^5W\)-component of \(\delta\), leaving freely the \(v\wedge\bigwedge^4W\)-component of dimension \(5\). No higher-degree equations occur. Hence \(\dim K(u)=1+10+5=16\), giving centralizer dimension \(48\). There are \((q^6-1)q^{20+6}\) such odd elements.

**3. A nonzero trivector and vanishing degree-one part.** Suppose \(v=0\) and \(\alpha\ne0\). Define

\[k(\alpha)=\dim\{w\in V:w\wedge\alpha=0\}.\]

The degree-four equation requires \(w\wedge\alpha=0\). The degree-six equation is \(\alpha\wedge\beta+\gamma\wedge w=0\); as a functional of \(\beta\in\bigwedge^3 V\), \(\beta\mapsto\alpha\wedge\beta\) is nonzero by the perfect middle-dimensional wedge pairing. Thus \(\beta\) has \(19\) free parameters, \(\delta\in\bigwedge^5V\) has \(6\), and \(w\) has \(k(\alpha)\). It follows that

\[\dim K(u)=25+k(\alpha),\qquad \dim C_E(a)=57+k(\alpha).\]

We next classify the possible \(k(\alpha)\). If some nonzero \(w\) annihilates \(\alpha\), the standard direct-sum decomposition along the line \(\ell=\langle w\rangle\) shows \(\alpha=w\wedge\eta\), with \(\eta\in\bigwedge^2(V/\ell)\). If another independent vector annihilates \(\alpha\), the same decomposition modulo the first line forces \(\eta\) to have a linear factor; a nonzero \(3\)-vector divisible by two independent vectors is decomposable. Conversely a nonzero decomposable \(3\)-vector is annihilated by exactly the three-dimensional span of its factors. A nondecomposable \(\eta\) has alternating-matrix rank \(4\) in the five-dimensional quotient (rank \(2\) means decomposable), and then its induced annihilator is exactly \(\ell\). Therefore

\[k(\alpha)\in\{0,1,3\};\]

\(k=3\) means \(\alpha\) is decomposable, \(k=1\) means it has precisely one annihilating line, and \(k=0\) means no nonzero vector annihilates it.

Each decomposable trivector is a nonzero scalar on the exterior cube of a unique three-dimensional subspace. There are thus \(D_3=(q-1){6\brack3}_q\) such trivectors. For each line \(\ell\), the number of nonzero two-vectors on \(V/\ell\) is \(q^{10}-1\), of which \((q-1){5\brack2}_q\) are decomposable (alternating rank two). The others have rank four and yield precisely the unique-annihilator class. Counting by its unique line gives \(D_1\); the remaining nonzero trivectors number \(D_0\). Since \(\gamma\) is arbitrary, each nonzero-trivector stratum contributes a factor \(q^6\).

**4. Pure degree-five elements and zero.** If \(v=\alpha=0\) but \(\gamma\ne0\), wedge multiplication by \(\gamma\) on \(V\) has rank one, and no other odd degrees can produce a nonzero product. Thus \(\dim K(u)=31\), giving centralizer dimension \(63\), with \(q^6-1\) possible \(\gamma\). For \(u=0\), the odd kernel has dimension \(32\), giving centralizer dimension \(64\).

**5. Counting even components and commuting pairs.** Every odd element admits independently \(q^{32}\) even components, proving the six-row distribution. The rows sum to \(q^{64}\) algebra elements. The number of ordered commuting pairs is \(\sum_dN_dq^d\). Dividing by \(q^{128}\), substituting \(D_0,D_1,D_3\), and simplifying yields the displayed rational function. Its top term is \(q^{-13}\), while the next correction is of relative order \(q^{-3}\). This proves every assertion.

## Verification

The standalone standard-library script `verify.py` performs three independent finite checks: exact bitset enumeration of all \(2^{20}\) trivectors over \(\mathbb F_2\) for the characteristic-independent wedge-annihilator stratification; direct exterior-product matrix ranks over \(\mathbb F_3\) for all six representative cases and forty sampled odd elements; and Gaussian-binomial, distribution-total, and exact rational commuting-probability identities at \(q=3,5,7\). The bitset enumeration is a finite geometric check over characteristic two, **not** a claim about characteristic-two commuting probabilities. The output is:

`ALL_EXTERIOR_SIX_CENTRALIZER_CHECKS_PASSED [992496, 54684, 0, 1395, 0, 0, 1] [('nonzero degree one', 48), ('zero wedge-annihilator trivector', 57), ('one-dimensional wedge-annihilator', 58), ('decomposable trivector', 60), ('pure nonzero five-form', 63), ('zero odd part', 64)]`

The all-odd-prime-power assertion rests on the proof above, not on finite experiments.

## Relationship to prior work

Bovdi–Leung (2018, arXiv:1803.03457) and Domokos–Zubor (2014/2015, arXiv:1403.2916) investigate maximal commutative subalgebras of Grassmann algebras, including the graded-commutativity framework and the dimension of maximal commutative subalgebras in even generator rank. These established facts are used, not claimed as new. The result here instead concerns **every element-centralizer**, its precise frequency over each odd finite field, and the ring-element commuting probability. In particular, the maximal commutative dimension \(48\) is not asserted to be newly discovered.

De Bruyn–Kwiatkowski (2011–2013) survey and classify six-dimensional trivector orbits under linear and symplectic groups. Their framework is stronger concerning trivector orbits and provides a natural alternative route to the geometric rank strata. The elementary incidence counts for decomposable trivectors are likewise standard. The stated contribution is the resulting **complete centralizer spectrum and arithmetic multiplicities in the full, inhomogeneous exterior algebra**, plus the exact commuting law; no priority is claimed for the trivector orbit classification itself. General ring commuting probabilities are also treated by Juráš–Ursul (2022), for a different general-purpose problem.

## Limitations

The argument excludes characteristic two, where the exterior algebra is commutative. It does not classify element-centralizers up to subalgebra isomorphism or cover arbitrary generator rank. Finite verification does not establish the infinite field-size family. Although targeted published-material and mathematical-record searches found no equivalent explicit six-generator centralizer census, an unlocated derivation under a representation-theoretic or Grassmann-invariant formulation remains a residual historical-priority risk.

## References

1. V. A. Bovdi and H.-H. Leung, *Maximal commutative subalgebras of a Grassmann algebra*, arXiv:1803.03457 (first public version 9 March 2018), https://arxiv.org/abs/1803.03457.
2. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916, https://arxiv.org/abs/1403.2916.
3. B. De Bruyn and M. Kwiatkowski, *On the trivectors of a 6-dimensional symplectic vector space*, Linear Algebra Appl. 435 (2011), 289–306, https://doi.org/10.1016/j.laa.2011.01.028; and *The classification of the trivectors of a 6-dimensional symplectic space: summary, consequences and connections*, Linear Algebra Appl. 438 (2013), 3516–3529, https://biblio.ugent.be/publication/3217932.
4. M. Juráš and M. Ursul, *On commuting probabilities in finite groups and rings*, J. Algebra Combin. Discrete Struct. Appl. 9 (2022), 9–15, https://arxiv.org/abs/2010.01188.
