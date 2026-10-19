# The first two nontrivial odd-period levels of the Gingerbreadman map

## Finding

For the classical piecewise-affine area-preserving plane map
\[G(x,y)=(1-y+|x|,\ x),\qquad (x,y)\in\mathbb R^2,\]
the complete inventory of **odd least periods at most eleven** is as follows. The only fixed point is \((1,1)\). There is no orbit of least period \(3\), \(7\), or \(9\); there are exactly two orbits of least period \(5\) and exactly two orbits of least period \(11\), counting orbits rather than their points. In particular, **eleven is the next realized odd least period after five**.

The two period-five cycles admit lexicographically minimal representatives \((-1,1)\) and \((-1,-1)\). Their return-map derivative traces are respectively \(3\) and \(1\), so the first is hyperbolic and the second elliptic (its linear return has eigenvalues \(e^{\pm i\pi/3}\)). The period-eleven cycles have representatives
\[(-\tfrac13,\tfrac13)\quad\text{and}\quad(-\tfrac37,\tfrac57),\]
and return-map traces \(5\) and \(-5\), respectively. **Both period-eleven cycles are hyperbolic saddles**. In all these cycles the entire orbit avoids the nonsmooth line \(x=0\), making the derivatives unambiguous.

## Assumptions and scope

The map has the exact offset and unit scaling shown above, with no free parameters; it acts on **all of \(\mathbb R^2\)**, not only a plotted region, trapping hexagon, or invariant annulus. The *least period* of \(p\) is the smallest positive integer \(n\) for which \(G^n(p)=p\). Two points of the same cycle count as one orbit. Only odd least periods \(\le 11\) are classified; no conclusion about periods larger than eleven or even least periods is made.

## Proof

Put \(M_+=\begin{pmatrix}1&-1\\1&0\end{pmatrix}\), \(M_-=\begin{pmatrix}-1&-1\\1&0\end{pmatrix}\), and \(c=(1,0)^\mathsf T\). On the closed right or left branch, \(G(z)=M_s z+c\) for \(s\in\{+1,-1\}\), where at \(x=0\) both descriptions agree. In particular, \(\det M_s=1\).

For a fixed word \(w=(s_0,\ldots,s_{n-1})\) of length \(n\), define integer matrices and vectors recursively by
\[A_0=I,\quad d_0=0,\qquad A_{j+1}=M_{s_j}A_j,\quad d_{j+1}=M_{s_j}d_j+c.\]
A point \(z=(x,y)\) follows this itinerary and is \(n\)-periodic exactly when
\[s_j\,e_1^\mathsf T(A_jz+d_j)\ge0\quad(0\le j<n),\qquad (I-A_n)z=d_n.\]
These are integer-coefficient linear weak inequalities, after representing each equality by a pair of opposite inequalities. The inequalities are **necessary and sufficient**, including points on the switching line. Thus all \(2^n\) sign words enumerate **every** possible period-dividing-\(n\) point globally.

For completeness, the embedded standard-library checker performs exact two-variable Fourier–Motzkin elimination. Represent a halfspace by the integer triple \((a,b,c)\) signifying \(ax+by+c\ge0\). To eliminate \(x\), keep the triples with \(a=0\) and, for each triple \(p\) with positive \(a\) and triple \(m\) with negative \(a\), append \((-m_a)p+p_a m\). This is the exact projection to the remaining variable: every lower bound meets every upper bound, and absent one sign imposes no further restriction. Repeat for \(y\), and declare feasibility exactly when all resulting constants are nonnegative. Dividing triples by their **positive** common gcd changes neither inequalities nor feasibility. Every arithmetic operation is integral; no tolerance, finite-coordinate search window, or floating-point approximation is used.

For each feasible word, the same computation checks \(\det(I-A_n)\ne0\), solves the resulting unique point over \(\mathbb Q\), and directly checks its branch inequalities and recurrence. This is also a complete check that no feasible itinerary defines a positive-dimensional continuum at the chosen odd periods. The exhaustive verified table is:

| \(n\) | Branch words | Feasible words | Distinct solutions of \(G^n(z)=z\) | New orbits of least period \(n\) |
|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 | 1 |
| 3 | 8 | 1 | 1 | 0 |
| 5 | 32 | 11 | 11 | 2 |
| 7 | 128 | 1 | 1 | 0 |
| 9 | 512 | 1 | 1 | 0 |
| 11 | 2048 | 23 | 23 | 2 |

Since five and eleven are prime, their nonfixed solutions automatically have these least periods. Direct exact iteration of the two representatives at each period supplies the full cycles, while evaluating \(\operatorname{tr}(A_5)\) and \(\operatorname{tr}(A_{11})\) yields \((3,1)\) and \((5,-5)\), respectively. The determinants are one. Consequently, period-eleven multipliers satisfy \(\lambda+\lambda^{-1}=\pm5\), which implies hyperbolic saddle type. All listed orbit coordinates have nonzero first coordinate. This proves the claim.

## Verification

Run `python3 verify.py` with a normal Python 3 installation; no third-party packages, network access, or external files are required. The checker reproduces every row of the exhaustive table, the four canonical representatives, the derivative traces, and the final marker `EXACT_ODD_PERIOD_CENSUS_OK`. The embedded `CHECKS.txt` is the expected exact output, not a substitute for running the code. The proof of Fourier–Motzkin projection and the finite integer search specification above justify how exhaustive computation entails a global statement on \(\mathbb R^2\).

## Relationship to prior work

Devaney introduced this same map and its polygonal zones of instability in 1984 [1]. The accessible abstract describes the invariant polygons and elliptic fixed point, but the original paper's complete text could not be inspected; an earlier enumeration of period-eleven saddles there is a real residual priority risk. The MathWorld Gingerbreadman discussion [2] identifies the familiar outer period-five orbit \((-1,-1)\) and nearby period-thirty islands; its single-period-five statement is specific to the discussed island regions rather than a proved whole-plane count. Zolkin, Kharkov and Nagaitsev [3] analyze polygon-invariant symplectic maps and discuss the same Gingerbreadman example in relation to islands and rotation numbers. Their inspected comparison does not give the whole-plane primitive odd-period census or the two explicit period-eleven saddle traces. The present result is an exhaustive global finite odd-period classification, **not** a new discovery of the map, invariant hexagons, or the classical period-five island chain.

## Limitations

This is a finite cutoff theorem, not an asymptotic orbit growth law or a classification of all periods; it makes no claim about stability of trajectories other than the listed return-map spectra. The exhaustive checker certifies only the specified six values of \(n\); extrapolations are unproved. The original 1984 full paper could not be reviewed, so historical priority is not conclusively established. Bibliographic evidence dates that foundational paper to **March 1984**, without establishing the exact day of release; the machine date `1984-03-01` elsewhere in the package is **month-start encoding** of this month-granular evidence, not an asserted verified day of publication.

## References

1. R. L. Devaney, “A Piecewise Linear Model for the Zones of Instability of an Area-Preserving Map,” *Physica D* **10** (1984), 387–393. DOI: `10.1016/0167-2789(84)90187-8`.
2. E. W. Weisstein, “Gingerbreadman Map,” *MathWorld*, `https://mathworld.wolfram.com/GingerbreadmanMap.html`.
3. T. Zolkin, Y. Kharkov, S. Nagaitsev, “Machine-assisted discovery of integrable symplectic mappings,” arXiv:`2201.13133` (2022), published in *Physical Review Research* **5**, 043241 (2023), DOI: `10.1103/PhysRevResearch.5.043241`.
