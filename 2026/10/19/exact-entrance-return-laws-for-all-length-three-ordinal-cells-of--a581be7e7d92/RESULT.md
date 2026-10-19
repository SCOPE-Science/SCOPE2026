# Exact entrance-return laws for all length-three ordinal cells of the doubling map

## Finding
Let \(T:[0,1)\to[0,1)\) be \(T(x)=2x\pmod 1\) with Lebesgue invariant probability. For almost every \(x\), assign the three-point ordinal symbol \(s(x)=ijk\) when
\[T^i x<T^j x<T^k x,\qquad\{i,j,k\}=\{0,1,2\}.\]
Use the six ordered symbols \(012,201,021,120,102,210\). An **entrance** into symbol \(i\) at time \(n\) means \(s(T^n x)=i\) but \(s(T^{n-1}x)\ne i\). Condition on being at an entrance at time zero in the stationary natural extension of the dyadic system, and let \(R_i\) be the number of iterates until the next entrance into the *same* symbol. Thus staying in one symbol for several steps does **not** count as another entrance. For \(|z|\le1\), the exact probability generating functions \(G_i(z)=\mathbb E[z^{R_i}]\) have only three distinct values:
\[
\begin{aligned}
G_{012}(z)=G_{210}(z)&=\frac{z^3}{8-8z+z^3},\\
G_{201}(z)=G_{102}(z)&=\frac{z^2(4-2z-z^2)}{16-16z+2z^3-z^4},\\
G_{021}(z)=G_{120}(z)&=\frac{z^2}{4-2z-z^2}.
\end{aligned}
\]
In the same order, the exact pairs (mean entrance interval, variance) are
\[(8,24),\qquad (12,188),\qquad (6,22).\]
Consequently the two least frequent ordinal symbols \(201\) and \(102\) have overdispersed entrance intervals relative to the geometric law with the same mean (\(188>132\)), whereas the other four symbols have underdispersed intervals (\(24<56\) and \(22<30\)). These formulas determine every entrance-return probability, not only the first moments.

## Assumptions and scope
The observable is the identity on the interval; successive observations occur at unit lag, and a pattern means the chronological indices ordered by *increasing* value. Tied observations and discontinuity boundaries form a countable null set after all forward and backward preimages; choose arbitrary symbols on that set. Expectations are conditional on an actual entrance into the specified ordinal cell under the stationary two-sided symbolic process, **not** on an arbitrary point of the cell and **not** on a fresh independent sample at every time. All statements are exact for the standard fair dyadic map and all \(n\ge1\). No stochastic perturbation, arbitrary integer base, or different ordinal window length is asserted.

## Proof
**Step 1: exact ordinal partition.** Compare \(x,T(x),T^2(x)\) on the monotone branches of \(T\) and \(T^2\). Apart from the null boundary set the six cells, in increasing spatial order, are
\[
\begin{array}{c|cccccc}
\text{symbol}&012&201&021&120&102&210\\\hline
I_i &[0,1/4)&[1/4,1/3)&[1/3,1/2)&[1/2,2/3)&[2/3,3/4)&[3/4,1)
\end{array}.
\]
The corresponding Lebesgue masses are \((1/4,1/12,1/6,1/6,1/12,1/4)\).

**Step 2: exact Markov transition law.** Each \(T(I_i)\) is, up to endpoints, the union of whole cells: in the above order the image-index sets are \(\{0,1,2\},\{3\},\{4,5\},\{0,1\},\{2\},\{3,4,5\}\). Because \(T\) has slope \(2\) on every cell, the transition matrix for the stationary ordinal-symbol process is
\[
P=\begin{pmatrix}
1/2&1/6&1/3&0&0&0\\
0&0&0&1&0&0\\
0&0&0&0&1/4&3/4\\
3/4&1/4&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&1/3&1/6&1/2
\end{pmatrix}.
\]
Indeed, for each allowed edge \(i\to j\), the conditional probability is \(|I_j|/(2|I_i|)\). More importantly, conditioning on any admissible finite sequence of earlier cells leaves the *current position* uniform on its current cell: the relevant cylinder is mapped linearly and bijectively onto that cell. This proves the exact Markov property rather than merely using a heuristic stochastic approximation. In particular, conditioning on an entrance into cell \(i\) gives the uniform law on \(I_i\). The displayed matrix is irreducible and has self-loops, so its entrance-return times are almost surely finite.

**Step 3: first-entrance renewal formula.** Fix a cell \(i\), remove its row and column from \(P\) to obtain the \(5\times5\) substochastic matrix \(Q_i\), and put \(a_i=(P_{ij})_{j\ne i}\) (a row) and \(b_i=(P_{ji})_{j\ne i}\) (a column). To have the next entrance, a path may first spend any number \(k\ge0\) of steps staying in cell \(i\), must then exit, remain in the other cells for some number of steps, and finally hit cell \(i\). Consequently, for \(|z|<1\),
\[
G_i(z)=\frac{z^2}{1-zP_{ii}}\,a_i(I_5-zQ_i)^{-1}b_i.
\]
Expanding \((I_5-zQ_i)^{-1}\) as a nonnegative matrix series explicitly enumerates every possible first-entrance itinerary, so no unproved independence of successive symbols is needed beyond the established Markov property. Reflection \(x\mapsto1-x\) interchanges the cells in pairs \((0,5),(1,4),(2,3)\) and commutes with \(T\) modulo the endpoints. Direct elimination of the five linear hitting equations for \(i=0,1,2\), respectively, yields the three rational functions in the finding. Equivalently, multiplying the formulas by their denominators gives the complete recurrences
\[
\begin{aligned}
(8-8z+z^3)G_{012}(z)&=z^3,\\
(16-16z+2z^3-z^4)G_{201}(z)&=4z^2-2z^3-z^4,\\
(4-2z-z^2)G_{021}(z)&=z^2.
\end{aligned}
\]
Together with the known matrix formula, these polynomial identities can also be checked by substitution into the six-state hitting equations.

**Step 4: moments and entry intensity.** All three generating functions have \(G_i(1)=1\). Differentiating the displayed rational identities at \(z=1\) gives \(\mathbb E R_i=G_i'(1)\) and \(\operatorname{Var}(R_i)=G_i''(1)+G_i'(1)-G_i'(1)^2\), producing exactly \((8,24),(12,188),(6,22)\). Independently, the invariant mass of entry events is \(|I_i|(1-P_{ii})\), respectively \(1/8,1/12,1/6\), and its reciprocal equals each computed mean. The geometric comparator with positive-integer mean \(m\) has variance \(m(m-1)\), giving the final strict comparisons.

## Verification
Run `python3 verify_ordinal.py` with the included standalone Python 3 checker. It uses exact rational arithmetic to reconstruct all six ordinal cells and transition rows, computes the initial ten coefficients of each candidate generating function, and **independently** enumerates exact initial-coordinate intervals satisfying the first-entrance condition through time ten. All 60 coefficient comparisons agree. It also verifies the means and variances using polynomial differentiation and separately checks the stationary entrance-intensity identity. These are finite consistency tests; the proof of every coefficient for arbitrarily large return time is the renewal identity with the exact six-state Markov partition, not the finite enumeration.

## Relationship to prior work
Shahriari, Algar, Walker and Small [1] introduce ordinal selections of Poincaré sections, a chronological index ranking, and entropy-based ways to compare sections. Their published analysis emphasizes reconstruction of first-return maps from Lorenz, Rössler, and Mackey–Glass time series. The complete six-symbol *entrance-time distributions* of the dyadic map are a distinct, exactly computable calibration target for the same natural ordinal segmentation. Sakellariou, Stemler and Small [2] study ordinal-partition networks for estimating topological entropy, rather than the entrance-time probability laws computed here. Classical finite-state Markov renewal theory supplies the general matrix method used in Step 3, but the particular ordinal partition, three exact rational laws, and their variance trichotomy require the model-specific analysis in Steps 1–4. The latter, not general existence of a rational return generating function, is the claimed contribution.

## Limitations
This is an exact result for one canonical map and the smallest window with six ordinal symbols. It does not show which ordinal choice is optimal for detecting a physical attractor in noisy or continuous-time experiments. Other works on return-word and Markov-hole statistics might implicitly encode these rational formulas; an exhaustive historical priority search has not been established. The symbolic process is a special exact Markov example; most observed ordinal processes need not be Markov of order one. Independent validation has not been performed.

## References
[1] Z. Shahriari, S. D. Algar, D. M. Walker, M. Small, *Ordinal Poincaré Sections: Reconstructing the First Return Map from an Ordinal Segmentation of Time Series*, arXiv:2303.00383, first submitted 2023-03-01; *Chaos* **33**, 053109 (2023), DOI:10.1063/5.0141438. https://arxiv.org/abs/2303.00383

[2] K. Sakellariou, T. Stemler, M. Small, *Estimating topological entropy using ordinal partition networks*, *Physical Review E* **103**, 022214 (2021), DOI:10.1103/PhysRevE.103.022214. https://doi.org/10.1103/PhysRevE.103.022214

[3] C. Bandt, F. Shiha, *Order Patterns in Time Series*, *Journal of Time Series Analysis* **28**, 646–665 (2007), DOI:10.1111/j.1467-9892.2007.00528.x. https://doi.org/10.1111/j.1467-9892.2007.00528.x
