# An exact hidden bias-reversal surface in the four-site one-vacancy exclusion process

## Finding

In the periodic site-trap asymmetric simple exclusion process with four sites, **three particles and one vacancy**, let the positive site escape rates in cyclic order be \(a,b,c,d\), and let the external bias be \(|\varepsilon|<1\). A particle of site rate \(h_i\) hops right/left, when the destination is vacant, at rates \(h_i(1\pm\varepsilon)/2\). Let \(J(\varepsilon)\) be the stationary signed particle current **per bond**. Define

\[
U=a+c,\quad V=b+d,\quad x=a-c,\quad y=b-d,
\]
\[
P(\varepsilon)=UV(U+V)(1+\varepsilon^2)-2\varepsilon^2(Uy^2+Vx^2)+\varepsilon(1-\varepsilon^2)xy(U-V).
\]

Then the exact stationary current is

\[
\boxed{J(\varepsilon)=\frac{4abcd\,\varepsilon(1+\varepsilon^2)}{P(\varepsilon)}.}
\]

The denominator is strictly positive for all positive escape rates and every \(|\varepsilon|<1\). Hence **full bias-reversal symmetry, at every admissible bias**, is classified by

\[
\boxed{J(\varepsilon)=-J(-\varepsilon)\ \text{for all }|\varepsilon|<1
\quad\Longleftrightarrow\quad (a-c)(b-d)(a+c-b-d)=0.}
\]

The cases \(a=c\) and \(b=d\) arise from geometric reflections. In contrast, the balanced opposite-sums condition \(a+c=b+d\) allows all four escape rates to be distinct and therefore need not involve any reflection or spatially uniform bond-bias ratio. For example, with cyclic rates \((a,b,c,d)=(1,2,4,3)\), the exact current is

\[
\boxed{J(\varepsilon)=\frac{96\varepsilon(1+\varepsilon^2)}{250+150\varepsilon^2},}
\]

which is odd at every bias despite the absence of a geometric inversion. This is a **sector-specific** statement for three particles and does not restore the stronger simultaneous bias-reversal and particle-hole identities at all densities.

The complete even-in-bias part is

\[
\boxed{\frac{J(\varepsilon)+J(-\varepsilon)}2
=-\frac{4abcd\,\varepsilon^2(1-\varepsilon^4)xy(U-V)}{P(\varepsilon)P(-\varepsilon)}.}
\]

In particular,

\[
\boxed{[\varepsilon^2]J=-\frac{4abcd\,xy(U-V)}{U^2V^2(U+V)^2}.}
\]

Outside the three exact symmetry surfaces, the sign of the even current is the fixed sign of \(-xy(U-V)\) for **every** \(0<|\varepsilon|<1\): there are no finite-bias reversals of the rectification sign in this one-vacancy four-site model.

## Assumptions and scope

All four site escape rates are strictly positive constants. There are exactly three exclusion particles on a labeled four-site periodic nearest-neighbor ring. The bias satisfies \(-1<\varepsilon<1\), so all permitted transitions have positive rates and the four-state vacancy chain is irreducible. The current is stationary expected clockwise jumps minus counterclockwise jumps, divided by four; it is not the total jump rate. No thermodynamic limit, random averaging over the rates, or other particle-number sector is assumed.

## Proof

**Vacancy reduction.** Label the unique vacant site by \(i\in\mathbb Z/4\mathbb Z\). Its counterclockwise transition \(i\to i-1\) is caused by a clockwise particle jump from \(i-1\), and its clockwise transition \(i\to i+1\) is caused by a counterclockwise jump from \(i+1\). Thus, in the column-generator convention, the only off-diagonal entries are

\[
Q_{i-1,i}=\frac{h_{i-1}(1+\varepsilon)}2,\qquad
Q_{i+1,i}=\frac{h_{i+1}(1-\varepsilon)}2,
\]

with \(Q_{ii}\) equal to minus the sum of outgoing rates. All indices are modulo four. The stationary distribution is unique.

**Exact tree identity.** Let \(Q^{(i)}\) be the \(3\times3\) principal matrix obtained from \(Q\) by deleting row and column \(i\), and set \(w_i=-\det Q^{(i)}\). By the Markov-chain tree theorem these weights are strictly positive and \(\pi_i=w_i/\sum_jw_j\). Substituting the transition rates and expanding the four three-by-three determinants gives two exact polynomial identities:

\[
\sum_{i=0}^3w_i=\frac{P(\varepsilon)}8,
\]
\[
\frac14\sum_{i=0}^3 w_i
\left(\frac{h_{i-1}(1+\varepsilon)}2-\frac{h_{i+1}(1-\varepsilon)}2\right)
=\frac{abcd\,\varepsilon(1+\varepsilon^2)}2.
\]

The second equality is the *unnormalized* stationary particle current per bond. Dividing it by the first gives the displayed exact current. The code in the verification section reconstructs both identities from the four-state generator rather than assuming them.

**Positivity and necessity.** Every directed spanning in-tree uses only positive transition rates under the assumptions, and at least one such tree exists for every root; therefore every \(w_i>0\) and \(P=8\sum_iw_i>0\). Subtract the formulas at opposite biases. Their even part is precisely the stated factorization. Since \(a,b,c,d>0\), \(P(\pm\varepsilon)>0\), and \(\varepsilon^2(1-\varepsilon^4)>0\) for \(0<|\varepsilon|<1\), the even part vanishes identically if and only if \(xy(U-V)=0\). For the same reason, its sign cannot change at any nonzero admissible bias if that product is nonzero. Evaluating its second derivative at zero proves the quadratic coefficient.

**Non-geometric witness.** At \((1,2,4,3)\), \(U=V=5\) while \(a\ne c\) and \(b\ne d\). All rates are distinct, so no nontrivial dihedral reflection preserves the site-dependent hopping rates. Moreover, \(p_i(\varepsilon)/q_{i+1}(\varepsilon)=((1+\varepsilon)/(1-\varepsilon))h_i/h_{i+1}\) is not spatially constant. The explicit current nevertheless has exact oddness for all biases. This is not a contradiction to a condition posed *jointly for all particle densities*.

## Verification

Run `python verification.py` with SymPy installed. The standalone script builds the exact four-state generator from allowed three-particle exclusion moves and computes all stationary cofactors. It independently verifies the polynomial denominator and current, their even part and quadratic response coefficient, and the all-distinct balanced example. It also constructs the three-site single-particle and two-particle sectors to check the small-ring contrast. The verification gives **21 exact and finite checks**. The infinitely many bias values and all positive escape-rate parameters are covered by the algebraic proof above, not by numerical sampling.

## Relationship to prior work

Sakai and Akimoto's *Symmetry Breaking of Current Response in Disordered Exclusion Processes* (arXiv:2512.03316; earliest version dated 2025-12-03) defines precisely this quenched site-trap exclusion process. Their Sections III.1 and III.4 distinguish uniform bond-bias ratios and spatial inversion as robust symmetry mechanisms, and discuss the generic appearance of a quadratic asymmetric response otherwise. The present result gives a further **exact, all-bias, nonreflective** symmetry surface in one fixed high-density sector. It does not dispute their structural implication involving simultaneous symmetry relations for **all** densities.

Derrida's 1983 exact formula for the drift of a periodic one-dimensional nearest-neighbor walker covers the general vacancy reduction and therefore subsumes the *raw stationary-current calculation*. The contribution asserted here is **not** a new general one-walker velocity theorem; it is the explicit necessary-and-sufficient **all-bias parity classification**, the geometric versus non-geometric decomposition, and the bias-independent rectification-sign law for the physically motivated four-site exclusion sector. Earlier finite four-ring calculations in the two-particle sector analyze different response cancellations and do not establish these three-particle all-order statements. The exact formula is an algebraic specialization of established walk theory; that priority limitation is substantive.

## Limitations

The result is confined to a four-site ring with three particles and positive fixed site-escape rates. It does not claim analogous symmetry surfaces for arbitrary system sizes, other fillings, different environmental models, time-dependent drive, or the thermodynamic limit. The algebraic parity classification is derived from a known general periodic-walk formula (and can equivalently be established by the self-contained four-state tree calculation), so its claimed originality is the evaluated structural consequence rather than stationary solvability itself. Independent literature-wide priority review has not occurred.

## References

1. I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1 (2025-12-03), https://arxiv.org/abs/2512.03316.
2. B. Derrida, *Velocity and Diffusion Constant of a Periodic One-Dimensional Hopping Model*, Journal of Statistical Physics 31 (1983), 433–450, doi:10.1007/BF01019492, https://www.lps.ens.fr/~derrida/PAPIERS/1983/jsp1983-vitesse.pdf.
