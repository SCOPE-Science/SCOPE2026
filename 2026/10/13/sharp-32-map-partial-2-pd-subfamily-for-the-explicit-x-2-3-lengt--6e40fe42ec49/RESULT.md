# Sharp 32-map partial 2-PD subfamily for the explicit \(X_{2,3}\) length-128 AG code
## Finding
Consider the explicit one-point code \(C(D,67P_\infty)\) on the generalized Hermitian curve
\[
X_{2,3}:\quad y^2+y=x^9
\]
over \(\mathbb F_{64}\) from Example 4.6 of Castellanos--Tizziotti--Olaya-León, with the information/check positions supplied by Proposition 3.7 and the orbit ordering of Example 3.5.  Let \(\mathcal F\) be the \(128\)-element partial \(2\)-PD set supplied by Theorem 4.5 for this code.

The minimum cardinality of a subfamily \(\mathcal S\subseteq\mathcal F\) that is still a partial \(2\)-PD set for these fixed information/check positions is exactly
\[
|\mathcal S|_{\min}=32.
\]
Thus the source's displayed \(128\)-map construction can be reduced by a factor of four for its explicit length-128 example, and no further reduction is possible while staying inside the same Theorem 4.5 automorphism family and keeping the same information set.

## Assumptions and scope
Write the source orbits as \(O_j(t)\), where \(t\in\{1,\ldots,9\}\) indexes the displayed order inside each length-9 orbit.  For \(\lambda=67\), Proposition 3.7 gives the \(64\) information positions
\[
I=O_1\cup\cdots\cup O_6
 \cup\{O_7(1),\ldots,O_7(7)\}
 \cup\{O_8(1),O_8(2),O_8(3)\},
\]
and the check set is \(H=D\setminus I\), also of size \(64\).

For \(a\in\mathbb F_{64}\), define
\[
\omega_a(x)=a^{32}x^4+a^{16}x^2+a^8x.
\]
In characteristic two, the source family can be written without making the arbitrary choice of one root \(b_a\) as
\[
\Phi_{a,c}(x,y)=(x+a,\ y+\omega_a(x)+c),
\]
where \(c+\omega_a(a)\) is one of the two roots of \(z^2+z=a^9\).  There are exactly two such constants \(c\) for each \(a\), giving the \(128\) maps of \(\mathcal F\).

The claim is only about subfamilies of this specific \(\mathcal F\) and this fixed source information set.  It does not claim a minimum over the full permutation automorphism group of the code, over other information sets, or over monomial automorphisms.

## Proof
For each \(x\in\mathbb F_{64}\), let
\[
V_x=\{(x,y)\in X_{2,3}(\mathbb F_{64}):y^2+y=x^9\}.
\]
Every \(V_x\) has two points.  Reading the check set above against the orbit table of Example 3.5 shows that exactly three vertical fibers lie wholly in \(H\):
\[
V_0,\qquad V_1,\qquad V_{\theta^{56}}.
\]
Indeed, \(V_0=O_{15}\cup O_{16}\).  The two orbits \(O_7\) and \(O_{14}\) have the same first-coordinate cycle and supply the two points in each corresponding vertical fiber; \(O_{14}\subset H\), while only \(O_7(8)\) and \(O_7(9)\) are check positions, giving first coordinates \(\theta^{56}\) and \(1\).  Every other nonzero first-coordinate cycle pairs one information orbit with a check orbit or meets the partial orbit \(O_8\), so it contributes no further complete vertical fiber to \(H\).

Set
\[
T=\{0,1,\theta^{56}\},\qquad
W=\operatorname{span}_{\mathbb F_2}\{1,\theta^{56}\}.
\]
Since \(\theta^{56}\notin\mathbb F_2\), the set \(W\) has four elements and \(T\) is \(W\) with one point removed.  Each \(\Phi_{a,c}\) translates the first coordinate by \(a\), so the vertical pairs moved completely into \(H\) are exactly those with first coordinate in
\[
a+T.
\]
The \(64\) first-coordinate values split into \(16\) affine cosets of \(W\).  A set \(a+T\) is contained in one such coset and misses one of its four points.  Therefore one translation parameter cannot cover all four vertical pairs in its coset; at least two distinct translation parameters are required in each of the \(16\) cosets.  Any partial \(2\)-PD subfamily of \(\mathcal F\) must therefore have at least
\[
2\cdot16=32
\]
maps.  The two possible constants \(c\) for a fixed \(a\) do not change this vertical-fiber obstruction.

For the matching upper bound, the following \(32\) pairs \((a,c)\) define maps \(\Phi_{a,c}\in\mathcal F\):
\[
\begin{aligned}
&(0,1),\ (\theta^{56},\theta^{21}),\ (\theta^{49},\theta^{42}),\ (\theta^{57},\theta^{18}),\\
&(\theta^3,\theta^{59}),\ (\theta^{50},\theta^{54}),\ (\theta^{58},\theta^{36}),\ (\theta^{25},\theta^9),\\
&(\theta^4,\theta^{27}),\ (\theta^{35},\theta^{21}),\ (\theta^{51},\theta^{45}),\ (\theta^{54},\theta^{47}),\\
&(\theta^{31},\theta^{31}),\ (\theta^6,\theta^{62}),\ (\theta^{46},\theta^{27}),\ (\theta^{37},\theta^{36}),\\
&(\theta^{30},\theta^{36}),\ (\theta^{45},\theta^{59}),\ (\theta^{34},\theta^{55}),\ (\theta^{39},\theta^9),\\
&(\theta^{12},\theta^{47}),\ (\theta^{24},\theta^{31}),\ (\theta^{55},\theta^{55}),\ (\theta^{48},\theta^{55}),\\
&(\theta^{60},\theta^9),\ (\theta^{32},\theta^{27}),\ (\theta^9,\theta^{36}),\ (\theta^7,\theta^{21}),\\
&(\theta^{23},\theta^{36}),\ (\theta^{11},\theta^9),\ (\theta^{38},\theta^{59}),\ (\theta^{33},\theta^{47}).
\end{aligned}
\]
An exact exhaustive check over all \(\binom{128}{2}=8128\) unordered coordinate pairs verifies that at least one of these \(32\) maps sends each pair into \(H\).  Hence they form a partial \(2\)-PD set, and the lower bound proves optimality inside \(\mathcal F\).

## Verification
The included `verify.py` realizes \(\mathbb F_{64}\) as
\[
\mathbb F_2[\theta]/(\theta^6+\theta^4+\theta^3+\theta+1),
\]
a representative consistent with every point in the source's Example 3.5 orbit table.  It reconstructs all \(128\) affine points, the \(64/64\) information/check split, all \(128\) Theorem 4.5 maps, and all \(8128\) unordered coordinate pairs.

It independently checks that the full source family covers every pair, that the only vertical fibers wholly in \(H\) are those indexed by \(T\), that the \(16\) affine \(W\)-cosets force the lower bound \(32\), that each displayed witness map belongs to the source family, and that the displayed \(32\) maps cover every unordered pair.  All finite-field operations are exact bit-polynomial arithmetic; no floating-point computation, random sampling, or solver output is needed for the final certificate.

Changing to a Frobenius-conjugate realization of the primitive element transports the entire construction by a field automorphism, so the certificate is not tied to machine labels for field elements.

## Relationship to prior work
Castellanos--Tizziotti--Olaya-León construct the \(128\)-element partial \(2\)-PD family for special SAP curves and instantiate it on \(C(D,67P_\infty)\).  Their conclusion explicitly identifies construction of smaller PD sets and complexity analysis as directions for further study; it does not give a smaller subfamily or a minimum for Example 4.6.

Lichtenwalner--López--Matthews--Seneviratne earlier give permutation-decoding sets for Hermitian and norm-trace one-point codes.  In particular, their Hermitian Proposition 3.10 gives a \(2\)-PD set of size \(q(q^2-1)\).  That result concerns a different curve family and information-set construction and does not imply the exact \(32\)-map optimum for the generalized Hermitian example here.

The broader PD-set literature contains general lower bounds and examples where large automorphism-derived sets can be reduced for specific information sets.  Those principles motivate the optimization but do not determine the vertical-fiber incidence pattern or the exact optimum for this code.

## Limitations
The optimum \(32\) is relative to the \(128\) maps of Theorem 4.5 and the source's fixed information/check set.  A smaller partial \(2\)-PD set could conceivably exist using other code automorphisms or a different information set; that question is not addressed.  The result also does not claim that \(32\) is the Gordon/Schönheim minimum over arbitrary permutations.

The finite certificate proves coverage and the structural lower bound for the stated object.  It does not by itself establish absolute literature novelty; an unindexed equivalent computation remains a residual bibliographic risk.

## References
1. A. S. Castellanos, G. Tizziotti, W. Olaya-León, *Permutation Decoding of AG Codes from Curves Defined by Separated Polynomials*, arXiv:2608.03592v1, 4 August 2026.
2. M. Lichtenwalner, H. H. López, G. L. Matthews, P. Seneviratne, *Permutation decoding of algebraic geometry codes from Hermitian and norm-trace curves*, arXiv:2602.20455v1, 24 February 2026.
3. D. M. Gordon, *Permutation decoding and PD-sets*, Designs, Codes and Cryptography 38 (2006), 27--41.
4. D. Crnković, N. Mostarac, *PD-sets for codes related to flag-transitive symmetric designs*, Transactions on Combinatorics 7 (2018), 37--50, DOI: 10.22108/toc.2017.21615.
