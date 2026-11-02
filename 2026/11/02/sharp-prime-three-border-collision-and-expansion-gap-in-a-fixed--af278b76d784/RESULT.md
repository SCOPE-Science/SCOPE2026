# Sharp prime-three border collision and expansion gap in a fixed-point-free four-branch map

## Finding

For the normalized four-branch interval map \(F_{r,s}:[-s,s]\to[-s,s]\) defined below, with \(0<r<1\) and \(s>1\), the number \(N_3(r,s)\) of geometrically distinct orbits of **least period three** satisfies the complete classification
\[
N_3(r,s)=\begin{cases}0,&r(s-1)<1,\\1,&r(s-1)=1,\\2,&r(s-1)>1.\end{cases}
\]
At equality the unique orbit is \(\{0,-s,-1\}\). Above equality both orbits are strictly off all branch boundaries, have common return multiplier \(rs^2>4\), and are exact negatives of one another. Their coordinates, unique up to cyclic rotation, are
\[
X=\frac{r(s^2-s+1)}{rs^2-1},\qquad Y=s(X-1),\qquad Z=s(Y+1),
\]
with the first orbit \(\{X,Y,Z\}\), where \(0<X<1\), \(-1<Y<0\), \(1<Z<s\), and the other orbit \(\{-X,-Y,-Z\}\). The lower bound \(rs^2>4\) is sharp as an unattained infimum over the open existence region. The exact approach to the branch boundaries is
\[
1-X=\frac{r(s-1)-1}{rs^2-1},\quad -Y=\frac{s[r(s-1)-1]}{rs^2-1},\quad s-Z=\frac{s^2[r(s-1)-1]}{rs^2-1}.
\]
Thus the two cycles appear discontinuously at a border collision: as the threshold is approached from above one limiting three-point set is the actual boundary orbit, while its sign-reversed limit is not an orbit because the map assigns its jump value at zero to the right branch.

## Assumptions and scope

The map is
\[
F_{r,s}(x)=\begin{cases}
r(x+1),&-s\le x\le-1,\\
s(x+1),&-1<x<0,\\
s(x-1),&0\le x<1,\\
r(x-1),&1\le x\le s,
\end{cases}\qquad 0<r<1,\quad s>1.
\]
Every endpoint convention is part of the statement, particularly \(F_{r,s}(0)=-s\). It is immediate from the pieces that the image lies in \([-s,s]\). A geometric orbit means a set of three distinct points related cyclically by \(F_{r,s}\); cyclic changes of starting point are not counted anew.

This is an exact positive-rescaling of the piecewise-linear fixed-point-free map in García-Grimaldo and Campos-Cantón (2021), explicitly reprinted in García-Grimaldo and collaborators (2023). Their parameters are \(m_1=r\), \(m_2=s\), \(a=b_1/m_1>0\), \(b_2=s a\) and their state is \(a x\). The original map with \(b_1>0\) and the positive-slope assumptions is therefore conjugate by \(x\mapsto a x\) to the map above. The assumption \(b_1>0\) controls amplitude but not the orbit count or multipliers.

## Proof

**1. No fixed points and reduction to sign itineraries.** Every point in \((0,1)\) maps to a negative point, and every point in \((-1,0)\) maps to a positive point. Every \(x\in[1,s]\) maps strictly below itself, and every \(x\in[-s,-1]\) maps strictly above itself. The point zero maps to \(-s\). Hence there is no fixed point. Away from \(\{0,-1,1\}\), each visit to an inner branch changes sign, and each visit to an outer branch preserves sign. A three-cycle avoiding these three points must have an even number of inner visits. It cannot have zero such visits: all-three-outer iterations would preserve a sign, but each positive outer step strictly decreases its argument and each negative outer step strictly increases it. Therefore it has **exactly two inner visits and one outer visit**. This already exhausts all strict three-cycle itineraries.

If the outer visit is on the positive side, cyclically order the points as a positive inner point \(X\), a negative inner point \(Y\), then a positive outer point \(Z\). The equations are necessarily
\[
Y=s(X-1),\qquad Z=s(Y+1),\qquad X=r(Z-1).
\]
Solving yields the expressions stated in the finding, with denominator \(D=rs^2-1\). In particular \(X=r(s^2-s+1)/D\). Since \(s^2-s+1>0\), the required \(X>0\) forces \(D>0\). Now the required \(X<1\) is equivalent to \(r(s-1)>1\), because
\[
1-X=\frac{r(s-1)-1}{D}.
\]
Under \(r(s-1)>1\) one has \(D>0\), and the identities
\[
-Y=\frac{s[r(s-1)-1]}D,\quad Y+1=\frac{rs+s-1}D,
\quad Z-1=\frac{s^2-s+1}D,\quad s-Z=\frac{s^2[r(s-1)-1]}D
\]
show the strict branch inequalities \(-1<Y<0\) and \(1<Z<s\). Thus there is **exactly one** strict three-cycle whose outer visit is positive, precisely when \(r(s-1)>1\). Away from zero and the boundary, the map is odd: \(F_{r,s}(-x)=-F_{r,s}(x)\). Negation gives exactly one other strict three-cycle, whose outer visit is negative. These are disjoint because their outer points have opposite signs. If \(r(s-1)\le1\), neither strict itinerary is admissible.

**2. Endpoint orbits.** Because \(F_{r,s}(-1)=F_{r,s}(1)=0\), any periodic orbit meeting either outer/inner boundary also meets zero. The forward orbit from zero begins
\[
0\longmapsto -s\longmapsto-r(s-1).
\]
The only negative preimage of zero in \([-s,s]\) is \(-1\). Therefore a three-cycle through zero exists if and only if \(r(s-1)=1\), in which case it is exactly \(0\mapsto-s\mapsto-1\mapsto0\). This orbit has three different points. No other boundary three-cycle exists. Together with Step 1 this proves the census including its equality case.

**3. Expansion and sharpness.** On each strict cycle, the derivative product is \(s\cdot s\cdot r=rs^2\). In the strict existence region \(s>2\) and \(r>1/(s-1)\). Consequently
\[
rs^2>\frac{s^2}{s-1}=4+\frac{(s-2)^2}{s-1}>4.
\]
All these cycles are repelling. The bound four is sharp but unattained: take \(s=2+\varepsilon\) and choose \(r\) strictly between \(1/(s-1)\) and \(1\), tending to one as \(\varepsilon\downarrow0\). Then \(rs^2\to4\). The exact distances from the branch boundaries follow by the already-proved expressions. Approaching the threshold, the positive-outer orbit tends to \(\{1,0,s\}\), which is not an orbit because \(F(0)=-s\), while the negative-outer orbit tends to the actual orbit \(\{-1,0,-s\}\).

## Verification

The standalone file `verify.py` checks the exact algebraic composition, all five displayed coordinate identities, and 64 possible affine three-step itinerary words for each of 12 rational parameter pairs spanning the three regimes, including branch-boundary cases. It uses exact rational arithmetic for all orbit comparisons and independent branch selection. Execute `python verify.py` with Python 3 and SymPy. All 768 finite itinerary checks passed. These finite tests are independent checks of the formulas, **not a replacement** for the universal proof above. The inequalities, completeness of sign cases, and sharpness of the bound are proved analytically.

For example, at \((r,s)=(4/5,5)\), the first cycle is
\[
\left\{\frac{84}{95},-\frac{11}{19},\frac{40}{19}\right\},
\]
and the second is its negative. The return multiplier is exactly \(20\).

## Relationship to prior work

García-Grimaldo and Campos-Cantón (2021), DOI `10.1142/S021812742150200X`, introduced the map class and fixed-point-free/Devaney-chaos results. The public preview and abstract were accessible but the complete 16-page original could not be read here. García-Grimaldo and collaborators (2023), DOI `10.3390/electronics12020444`, reproduces the exact map and original fixed-point-free hypotheses. Its full text was inspected through its public author/publisher copy: Sections 2 and 3 establish the map, a specific Devaney-chaos instance, numerical parameter bifurcations, and examples of attracting periods four and six; they do not state this all-parameter period-three census or its sharp uniform expansion gap. The 2022 comparative chapter, DOI `10.1007/978-3-031-02472-6_8`, describes numerical bifurcation, Lyapunov, and entropy comparisons, but only its abstract could be read. The present calculation specializes to the positive-slope map and does not claim a general classification for all fixed-point-free maps.

## Limitations

The theorem assumes exactly the stated branches and endpoint convention, \(0<r<1\), \(s>1\), and positive amplitude scaling. It does not enumerate prime periods above three, characterize invariant measures, or assert Li–Yorke chaos based on an interval theorem requiring continuity. No stability multiplier is asserted at the discontinuous boundary orbit. The original 2021 full text and the 2022 comparative chapter were not fully accessible, leaving a residual publication-priority risk; a source search cannot prove priority. Independent mathematical audit has not been performed.

## References

1. C. García-Grimaldo and E. Campos-Cantón, *Chaotic Features of a Class of Discrete Maps without Fixed Points*, International Journal of Bifurcation and Chaos **31** (2021), 2150200. DOI: `10.1142/S021812742150200X`. First verified public source date used here: 2021-10-26 (MaRDI bibliographic record).
2. C. García-Grimaldo, C. F. Bermudez-Marquez, E. Tlelo-Cuautle and E. Campos-Cantón, *FPGA Implementation of a Chaotic Map with No Fixed Point*, Electronics **12** (2023), 444. DOI: `10.3390/electronics12020444`. Public full text inspected at `https://www.researchgate.net/publication/367172138_FPGA_Implementation_of_a_Chaotic_Map_with_No_Fixed_Point`.
3. C. García-Grimaldo and E. Campos-Cantón, *Comparative Analysis of Chaotic Features of Maps Without Fixed Points*, in *Complex Systems and Their Applications* (2022), DOI: `10.1007/978-3-031-02472-6_8`. Abstract inspected.
