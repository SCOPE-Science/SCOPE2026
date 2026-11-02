# A sharp two-zone double reversal in probabilistic retail site selection

## Finding

**Theorem (complete two-zone site-ranking phase diagram).** Consider two candidate retail locations, each evaluated *separately* as the one prospective entrant against the same fixed competing/outside attractiveness. Give the entrant a common variable intrinsic attractiveness \(t>0\). In demand zone \(i\), let \(p_i>0\) be purchasing power, \(w_i>0\) the fixed aggregate attraction of all alternatives, and \(a_i,b_i>0\) the attraction coefficients per unit entrant attractiveness at locations A and B. Set \(u_i=a_i/w_i\), \(v_i=b_i/w_i\), and

\[
S_A(t)=\sum_{i=1}^{m}p_i\frac{tu_i}{1+tu_i},\qquad
S_B(t)=\sum_{i=1}^{m}p_i\frac{tv_i}{1+tv_i}.
\]

For \(m=1\), the ordering of \(S_A(t)\) and \(S_B(t)\) is independent of \(t>0\). For arbitrary \(m\), unless the two captures agree identically, there are at most \(2m-2\) distinct positive investment levels at which the site captures tie.

For \(m=2\), if both zones prefer the same candidate locally (allowing equality in either zone), the total site ranking never changes. Otherwise relabel the zones so that \(u_1>v_1\) and \(u_2<v_2\), and put

\[
A_0=p_1(u_1-v_1)>0,\qquad B_0=p_2(v_2-u_2)>0,
\]
\[
c_0=A_0-B_0,\quad
c_1=A_0(u_2+v_2)-B_0(u_1+v_1),\quad
c_2=A_0u_2v_2-B_0u_1v_1.
\]

The preference between A and B reverses **twice** as \(t\) increases from zero to infinity if and only if

\[
\boxed{c_0c_2>0,\quad c_1c_2<0,\quad c_1^2>4c_0c_2.}
\]

When these conditions hold, the two distinct, positive thresholds are the roots of \(c_0+c_1t+c_2t^2=0\), and the same site wins at very low and very high investment while the other wins in between. Outside this regime there is at most one **strict** site-preference reversal on \((0,\infty)\), including possible double-root ties without a reversal. Identical capture at all investment levels occurs precisely, in the opposing-local-preference case, when \(p_1=p_2\), \(u_1=v_2\), and \(v_1=u_2\). The two-reversal regime is nonempty and open in the six positive two-zone parameters.

**Sharp, geographically realizable witness.** For \((p_1,p_2)=(1,5)\) and
\((u_1,v_1,u_2,v_2)=(9,1,2,3)\),

\[
\boxed{S_A(t)-S_B(t)=\frac{t(3t-1)(t-3)}{(1+t)(1+2t)(1+3t)(1+9t)}.}
\]

Thus A is preferred when \(0<t<1/3\), B when \(1/3<t<3\), and A again for \(t>3\). The two ties occur at exactly \(t=1/3\) and \(t=3\), with captures \(11/4\) and \(21/4\), respectively. One demand zone cannot exhibit any preference reversal, making **two zones the sharp minimum** for the double reversal.

## Assumptions and scope

The market has a fixed finite set of customer zones with strictly positive purchasing powers, a fixed incumbent or outside-option attraction in every zone, and two *mutually exclusive* candidate entrant sites. Entrant attractiveness scales linearly in one positive parameter while competitor attraction and demand remain fixed. The probabilistic market shares are proportional to entrant attraction among entrant and outside attraction, as in a unit-attractiveness-exponent Huff/gravity choice model. Attractiveness effects and travel impedance are included in fixed positive zone-specific coefficients. No competitor relocation, strategic response, site-dependent investment cost, or demand expansion is modeled. The result concerns expected captured purchasing power, not welfare or actual profit.

The geometry witness uses standard inverse-square distance decay, so its coefficients are not an arbitrary nonspatial construction. Put candidate sites at \(A=(0,0)\) and \(B=(1,0)\), and customer zones at

\[
z_1=\left(\frac1{18},\frac{\sqrt{35}}{18}\right),\qquad
z_2=\left(\frac7{12},\frac{\sqrt{23}}{12}\right).
\]

The squared distances to the two sites are \(1/9,1\) for zone 1 and \(1/2,1/3\) for zone 2, giving respectively \((9,1)\) and \((2,3)\) in inverse-square coefficients. Place an incumbent at the midpoint \(E=(z_1+z_2)/2\), and assign the incumbent fixed intrinsic attractiveness equal to \(\|z_1-E\|^2=\|z_2-E\|^2=(59-\sqrt{805})/432>0\). Then its inverse-square attraction equals exactly \(w_1=w_2=1\).

## Proof

**Step 1 (one-zone sign and the general bound).** A positive common denominator gives

\[
S_A(t)-S_B(t)=t\sum_{i=1}^{m}\frac{p_i(u_i-v_i)}{(1+u_it)(1+v_it)}.
\]

With one zone the sign is exactly the sign of \(u_1-v_1\) for every \(t>0\). With \(m\) zones, multiply by the strictly positive product \(\prod_{i=1}^m(1+u_it)(1+v_it)\). After removing the positive factor \(t\), the resulting polynomial has degree at most \(2m-2\). If nonzero it has at most that many positive zeros, counting multiplicities. This is a universal bound; no assertion of attainability for every \(m\) is made.

**Step 2 (two-zone reduction).** If \(u_i\ge v_i\) for both zones, every summand in the formula above is nonnegative; if the reverse, every summand is nonpositive. If there is opposition, exchange the two zone indices if necessary to arrange \(u_1>v_1\), \(u_2<v_2\). Write \(Q_1(t)=(1+u_1t)(1+v_1t)\) and \(Q_2(t)=(1+u_2t)(1+v_2t)\). Direct common-denominator reduction yields

\[
S_A(t)-S_B(t)=\frac{t[A_0Q_2(t)-B_0Q_1(t)]}{Q_1(t)Q_2(t)}
=\frac{t(c_0+c_1t+c_2t^2)}{Q_1(t)Q_2(t)}.
\]

Every factor in the denominator is positive for \(t>0\), so all positive-site comparisons reduce to the sign of the displayed quadratic.

**Step 3 (necessary and sufficient two-reversal criterion).** Two strict preference reversals require two distinct strictly positive simple roots of the quadratic. Hence \(c_2\ne0\), the discriminant \(c_1^2-4c_0c_2\) is strictly positive, the product of the two roots \(c_0/c_2\) is positive, and their sum \(-c_1/c_2\) is positive. These are exactly the three boxed strict inequalities. Conversely, these inequalities imply two distinct real roots with positive sum and positive product, hence both positive; a quadratic changes sign at both simple roots. A linear or constant polynomial has at most one reversal. A repeated root, a root at the excluded boundary \(t=0\), or a zero-free polynomial cannot generate two reversals.

If the quadratic vanishes identically, \(A_0Q_2=B_0Q_1\). Its constant coefficients imply \(A_0=B_0\), while its linear and quadratic coefficients imply that the unordered multisets \(\{u_1,v_1\}\), \(\{u_2,v_2\}\) coincide. Since the two local preferences have opposite strict directions, necessarily \(u_1=v_2\) and \(v_1=u_2\), and \(A_0=B_0\) then forces \(p_1=p_2\). Conversely, those conditions give identical capture for all \(t\).

**Step 4 (sharp witness and openness).** Substituting \(p_1=1,p_2=5,u_1=9,v_1=1,u_2=2,v_2=3\) gives \(A_0=8\), \(B_0=5\), hence

\[
A_0Q_2-B_0Q_1=8(1+5t+6t^2)-5(1+10t+9t^2)=3-10t+3t^2=(3t-1)(t-3).
\]

The roots and sign intervals follow. At this point all three inequalities in Step 3 are strict, so by continuity they hold on a neighborhood of the parameter tuple; the phenomenon is stable under small changes to positive purchasing powers and attractions. The Euclidean coordinates in the scope section give exactly these normalized coefficients. Thus the two-zone lower bound is attained even with genuine planar inverse-square attractiveness.

## Verification

The accompanying standalone \(\texttt{verify.py}\) requires only Python 3's standard library. Run it as \(\texttt{python verify.py}\). It checks the exact quadratic coefficients, exact roots, captured-market differences at three investment levels, positive-denominator identities on six thousand seeded exact-rational parameter tuples, the general Vieta sign criterion when applicable, and the squared-distance geometry. Floating-point measurements are used only as a high-precision corroboration of the midpoint geometry, which is proved algebraically in the text. The script performs 16,663 checks in its present configuration and prints PASS if all complete.

For the displayed witness the exact capture differences at \(t=1/6\), \(t=1\), and \(t=6\) are respectively \(17/420\), \(-1/60\), and \(306/95095\). These are independent evaluations of the two competing capture formulas. No finite search is used to prove the all-positive-parameter or all-\(m\) assertions: those follow from the rational identity and quadratic root argument.

## Relationship to prior work

Huff's 1963 gravity model already gives the probability-of-choice denominator and is not claimed as new. Drezner's 2014 open review explicitly discusses the Huff model, location search, attractiveness, budget allocation, and outside options; the full accessible article does not provide this exact two-zone continuously scaled **candidate-site ranking** phase diagram. Suárez-Vega, Santos-Peñate, and Dorta-González (2014) study joint location and quality on a network with a deterministic highest-attraction choice model rather than the fractional-choice model here. Drezner (2010) uses a Huff objective to analyze market share versus cannibalization; the accessible abstract does not establish the present crossover theorem, and its technical body was not accessible. Drezner and Drezner (2004) optimize Huff facility location with general continuous site search; only the abstract was accessible and its precise relationship to this two-candidate comparative-statics classification could not be fully resolved. A later open probabilistic-choice competitive-location study by Lin, Tian, and Zhao (2022) addresses endogenous demand and optimization, not the exact two-zone quadratic rank comparison reported here. Literature searches did not find an equivalent theorem, but absence from searches is not a mathematical originality certificate.

The mathematical contribution assessed here is the sharp condition for **two** ranking reversals in the smallest possible number of demand zones, with a spatially realizable witness. It is not a new probabilistic choice model, a global optimal-location algorithm, or a result about simultaneous entrants.

## Limitations

The classification is exact for expected market share under the specified deterministic parameters. It does not apply automatically if both candidates enter simultaneously, if competitors change their offer with entrant investment, if quality and distance are not separable as assumed, or if buying power, costs, or outside-option attraction vary with \(t\). It does not establish site profit maximization without a corresponding cost model. The general \(2m-2\) crossing bound need not be sharp for every \(m\). Historical priority for the two-zone result remains subject to further expert examination of inaccessible earlier primary texts. Independent audit has not been performed.

## References

1. D. L. Huff, "A Probabilistic Analysis of Shopping Center Trade Areas," *Land Economics* **39** (1963), 81–90. DOI: 10.2307/3144521. Original model; exact original first-public day not verified.
2. T. Drezner and Z. Drezner, "Finding the optimal solution to the Huff based competitive location model," *Computational Management Science* **1** (2004), 193–208. DOI: 10.1007/s10287-004-0009-6. Abstract available; full technical text unavailable.
3. T. Drezner, "Cannibalization in a Competitive Environment," *International Regional Science Review* **34** (2011), 306–322; first publicly available online 2010-12-30. DOI: 10.1177/0160017610389328. Abstract and references available; full technical text unavailable.
4. T. Drezner, "A review of competitive facility location in the plane," *Logistics Research* **7** (2014), article 114; online 2014-06-04. DOI: 10.1007/s12159-014-0114-z. Full open article examined.
5. R. Suárez-Vega, D. Santos-Peñate, and P. Dorta-González, "Location and quality selection for new facilities on a network market," *Annals of Regional Science* **52** (2014), 537–560. DOI: 10.1007/s00168-014-0598-0. Author-available full text examined.
6. Y. H. Lin, Q. Tian, and Y. Zhao, "Locating facilities under competition and market expansion: Formulation, optimization, and implications," *Production and Operations Management* **31** (2022), 3021–3042. DOI: 10.1111/poms.13737. Open full article examined as a later comparison.
