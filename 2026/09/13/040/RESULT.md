# Low-degree exterior-square twisted homology of configuration spaces of $\mathbb{CP}^{2}\#\mathbb{CP}^{2}$

## Setting and precise scope

Let $M=\mathbb{CP}^{2}\#\mathbb{CP}^{2}$ with its positive orientation. This is a closed simply connected smooth four-manifold with intersection form $\operatorname{diag}(1,1)$. Write $F_k(M)$ for ordered configurations, $B_k(M)=F_k(M)/S_k$, and
$$
V_k=\mathbb Q^k/\mathbb Q(1,\ldots,1),\qquad W_k=\Lambda^2V_k,\qquad \dim W_k=\binom{k-1}{2}.
$$
The covering determines the local system; $W_2=0$. For $k\ge3$, $W_k$ is the Specht representation of shape $(k-2,1,1)$.

This record gives a low-degree table, not the originally sought uniform slope-two stability theorem. It does not construct a geometric stabilization map for this closed manifold or supply a sharpness witness.

## Model and applicability

The rational Poincaré-duality algebra is
$$
A=H^*(M;\mathbb Q)=\mathbb Q[a,b,p]/(a^2-p,\ b^2-p,\ ab,\ ap,\ bp,\ p^2),
\qquad |a|=|b|=2,\quad |p|=4.
$$
A simply connected closed four-manifold is formal, so $A$ with zero differential is a rational model of $M$.

For rational cohomology as an $S_k$-representation, Lambrechts–Stanley (2008), Theorem 10.1 supplies exactly what is needed: for a closed oriented triangulated manifold and a connected Poincaré-duality CDGA $A$ connected to $A_{\mathrm{PL}}(M)$ by a quasi-isomorphism zigzag, its configuration complex $F(A,k)$ is equivariantly quasi-isomorphic as a differential graded module to $A_{\mathrm{PL}}(F_k(M))$. These hypotheses hold here. Only the resulting cohomology representations are used, not an additional claim about rational homotopy.

Idrissi's precise Theorem 95 gives an equivariant real CDGA model for simply connected closed smooth manifolds of dimension at least four. Framing and Euler-characteristic conditions restrict its further operadic/comodule enhancement, not the initial model statement. Corollary 116 is also applicable. We do not relabel this real theorem as a general rational-model theorem.

The complex has degree-three generators $G_{ij}=G_{ji}$, with
$$
dG_{ij}=\Delta_{ij}=p_i+p_j+a_i a_j+b_i b_j,\qquad
(x_i-x_j)G_{ij}=0\quad(x=a,b),
$$
and the exterior/Arnold relations. Permutations act on vertex labels. The positive signs match the intersection form.

Taking finite-group invariants is exact over $\mathbb Q$. Transfer gives
$$
H^i(B_k(M);W_k)\cong\bigl(H^i(F_k(M);\mathbb Q)\otimes W_k\bigr)^{S_k}.
$$
Since $W_k$ is self-dual, twisted homology is dual to this cohomology and has the same dimension.

## Result

For all $k\ge2$,
$$
H_i(B_k(M);W_k)=0\quad(0\le i\le3),\qquad
\dim H_4(B_k(M);W_k)=
\begin{cases}0&k=2,\\1&k\ge3.\end{cases}
$$
The surviving invariant is supported by the mixed-color family $a_i b_j$, $i\ne j$.

In degree five, after quotienting the model relations,
$$
H_5(B_k(M);W_k)=0\qquad(3\le k\le7).
$$
No all-$k$ degree-five vanishing is asserted.

The zero-edge degree-six contribution has dimension
$$
\dim\left[
\frac{(A^{\otimes k})^6\otimes W_k}
{d\bigl((A^{\otimes k})^2G\otimes W_k\bigr)}
\right]^{S_k}=2\qquad(3\le k\le6).
$$
The two-edge term $\Lambda^2G/(\text{Arnold relations})$ is omitted. This is not a claim that total $H_6$ has dimension two.

At the proposed degree-four boundary $k=2i+2=10$, both $k=10$ and $k=11$ have dimension one. This does not prove a map isomorphism or a sharpness witness.

## All-$k$ proof in degrees at most four

Let $f$ count fixed points and $m_2$ count two-cycles of a permutation. With $(f)_r=f(f-1)\cdots(f-r+1)$,
$$
\chi_{W_k}=\tfrac12(f)_2-f+1-m_2,\qquad
\chi_G=\tfrac12(f)_2+m_2,\qquad
\chi_{A^2}=2f,
$$
and
$$
\chi_{(A^{\otimes k})^4}=f+2\chi_G+(f)_2.
$$
The last character comprises $p_i$, the two same-color unordered-pair families, and the mixed-color ordered-pair family.

For a uniform permutation in $S_k$ the exact identity is
$$
\mathbb E[(f)_a(m_2)_b]=2^{-b}\quad\text{when }k\ge a+2b.
$$
Count ordered choices of $a$ fixed points and $b$ disjoint unordered two-cycles, then permute the remaining points. The support threshold is essential. Products relevant here have weighted degree at most four, so expansion into falling factorials gives for every $k\ge4$
$$
\langle1,W_k\rangle=\langle A^2,W_k\rangle
=\langle G,W_k\rangle=0,\qquad
\langle(A^{\otimes k})^4,W_k\rangle=1.
$$
Direct character evaluation gives the same result for $k=3$; $W_2=0$. The invariant complexes in degrees one, two and three vanish. In particular the degree-three invariant domain of the incoming degree-four boundary vanishes. Degree-four elements are closed, proving the table for all $k$.

The mixed-color term alone has multiplicity one; both the vertex term and the same-color pair terms have multiplicity zero. This identifies the surviving family.

## Degree-five quotient and finite exact certificate

Put $C_5=(A^{\otimes k})^2\otimes G\otimes W_k$ and $I=C_5^{S_k}$. Let $R$ be spanned by
$$
(a_l-a_m)G_{lm}\otimes w,\qquad (b_l-b_m)G_{lm}\otimes w.
$$
There are no other degree-five relations. Each column has a distinct color/edge/$W_k$-basis block, so
$$
\operatorname{rank}R=2\binom{k}{2}\binom{k-1}{2}.
$$
The diagonal identity proves $D(R)=0$; for example
$$
(a_l-a_m)\Delta_{lm}
=(a_l p_m-a_m p_l)+(p_l a_m-a_l p_m)=0.
$$
The $b_l b_m$ term vanishes by $ab=0$; the $b$ calculation is identical.

Exactness of averaging gives $(C_5/R)^{S_k}\cong I/(I\cap R)$, hence
$$
\dim H^5(B_k(M);W_k)=\dim I-\dim(I\cap R)-\operatorname{rank}(D|_I).
$$

| $k$ | $\dim I$ | $\operatorname{rank}R$ | $\dim(I\cap R)$ | $\operatorname{rank}(D|_I)$ | $\dim H^5$ | $\dim((A^{\otimes k})^6\otimes W_k)^{S_k}$ |
|---|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 6 | 2 | 0 | 0 | 2 |
| 4 | 4 | 36 | 2 | 2 | 0 | 4 |
| 5 | 4 | 120 | 2 | 2 | 0 | 4 |
| 6 | 4 | 300 | 2 | 2 | 0 | 4 |
| 7 | 4 | 630 | 2 | 2 | 0 | 4 |

The correct $k=3$ expression is $(2-2)-0=0$, not the reversed intermediate ranks in the preserved draft. The zero-edge degree-six dimension is the last column minus the incoming rank. Only $k=3,\ldots,6$ is its stated table; the extra $k=7$ calculation corroborates the method.

All finite ranks are exact rational linear algebra. Reynolds orbit sums enumerate every equality pattern of the five vertex roles of a free-domain basis monomial, so they span $I$. The degree-six enumeration similarly includes all color choices. The strengthened certificate verifies invariance under every adjacent transposition, including movement of the distinguished quotient index.

For an independent quotient calculation, identify $e_mG_{lm}$ with $e_lG_{lm}$ in each color/edge/$W_k$ block. This projection has kernel precisely $R$. Its rank on $I$ is zero for $k=3$ and two for $k=4,\ldots,7$, giving the intersection column without relying on the dense augmented-matrix implementation.

The new certificate independently multiplies the four diagonal terms with vertexwise ring rules, compares every free-domain basis image to the historical specialized differential, and checks all $6,36,120,300,630$ relation columns. It does not merely sample them. Exact integer Gram ranks then give the differential and degree-six invariant ranks.

## Reproducibility and retained evidence

From the package directory run artifacts/verify_low_degree.py with Python in UTF-8 mode. It asserts all finite ranks just listed. The historical final_checks.py provides finite character corroboration; boundary_k10_k11.py checks the degree-four boundary; h5_quotient.py and h5_quot_run7.py reproduce the dense rational quotient calculation. All were replayed in the fresh audit.

Historical scripts, including tentative stability and higher-degree investigations, are retained. Their exploratory comments, inherited incoming-rank constants and proposed map interpretations are not additional certified theorems. The only mechanical repairs to these scripts are stale artifact-path prefixes and explicit UTF-8 source reads.

## Prior work and limitations

The equivariant model is established mathematics, not claimed as new; it does not evaluate this specific isotypic quotient. Palmer's cited stability theorem requires an open connected manifold, whereas this table concerns a closed manifold. Inspected Félix–Tanré and Maguire computations concern ordinary unordered coefficients, not this exterior-square system on this connected sum. The closest Resultary match is this assigned item. Originality of the exact table is qualified to the best of our knowledge.

No total degree-six computation, higher-degree table, uniform $k\ge2i+3$ stability range or geometric-map identification is claimed. Degree-five vanishing is certified only through $k=7$. The full original target is not established.

## Primary references

1. P. Lambrechts and D. Stanley, *A remarkable DGmodule model for configuration spaces*, Algebraic & Geometric Topology 8 (2008), Theorem 10.1 and Definition 3.4: https://msp.org/agt/2008/8-2/agt-v8-n2-p21-p.pdf.
2. N. Idrissi, *The Lambrechts–Stanley model of configuration spaces*, arXiv:1608.08054, version 4, Theorem 95 and Corollary 116: https://arxiv.org/pdf/1608.08054.
3. M. Fernández and V. Muñoz, *The geography of non-formal manifolds*, Proposition 4.1 and proof: https://arxiv.org/pdf/math/0404527.
4. M. Palmer, *Twisted homological stability for configuration spaces*, arXiv:1308.4397.
5. Y. Félix and D. Tanré, *The cohomology algebra of unordered configuration spaces*, arXiv:math/0311323.
6. *Computing cohomology of configuration spaces*, arXiv:1612.06314.

