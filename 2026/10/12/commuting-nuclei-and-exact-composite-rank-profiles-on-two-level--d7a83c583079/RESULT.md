# Commuting nuclei and exact composite-rank profiles on two-level Heyting algebras
## Finding
For integers \(m,n\ge 2\), let \(P_{m,n}=A\oplus B\) be the ordinal sum of an \(m\)-point antichain \(A\) below an \(n\)-point antichain \(B\). Let \(H_{m,n}=\operatorname{Up}(P_{m,n})\), the finite Heyting algebra of upper sets ordered by inclusion. A **nucleus** is a monotone, extensive, idempotent, finite-meet-preserving map \(j:H_{m,n}\to H_{m,n}\).

All nuclei are indexed bijectively by subsets \(S\subseteq P_{m,n}\), according to
\[
j_S(U)=\{x\in P_{m,n}:\uparrow x\cap S\subseteq U\}.
\]
For \(S,T\subseteq P_{m,n}\), put \(S_A=S\cap A\), \(S_B=S\cap B\), and similarly for \(T\). The two nuclei commute **if and only if**
\[
(S_A\setminus T_A\ne\varnothing\ \Longrightarrow\ T_B\subseteq S_B),\qquad
(T_A\setminus S_A\ne\varnothing\ \Longrightarrow\ S_B\subseteq T_B).
\]
Whenever they commute, their composition is \(j_S\circ j_T=j_T\circ j_S=j_{S\cap T}\).

Define the **intersection-support profile** of ordered commuting pairs by
\[
F_{m,n}(x,y)=\sum_{(S,T):\,j_Sj_T=j_Tj_S}
 x^{|(S\cap T)\cap A|}y^{|(S\cap T)\cap B|}.
\]
Its complete closed form is
\[
\boxed{\begin{aligned}
F_{m,n}(x,y)={}&(1+x)^m(3+y)^n\\
&+2\bigl((2+x)^m-(1+x)^m\bigr)(2+y)^n\\
&+\bigl((3+x)^m-2(2+x)^m+(1+x)^m\bigr)(1+y)^n.
\end{aligned}}
\]
Equivalently, expansion yields the **level-exchange symmetry** \(F_{m,n}(x,y)=F_{n,m}(y,x)\). The total number of ordered commuting pairs is
\[
\boxed{C_{m,n}=2^m4^n+4^m2^n+2\cdot3^{m+n}-2\cdot2^m3^n-2\cdot3^m2^n+2^{m+n}.}
\]
A commuting pair with \(a=|(S\cap T)\cap A|\) and \(b=|(S\cap T)\cap B|\) has precisely \(2^a+2^b-1\) elements in the image of its composite. Thus the entire image-cardinality distribution is
\[
\boxed{R_{m,n}(z)=\sum_{a=0}^m\sum_{b=0}^n [x^ay^b]F_{m,n}(x,y)\,z^{2^a+2^b-1}.}
\]
In particular, \(R_{m,n}=R_{n,m}\): the endomorphism-free nucleus-composite rank census does not distinguish these nonisomorphic Heyting algebras when \(m\ne n\).

## Assumptions and scope
All posets and Heyting algebras here are finite. The order on \(P_{m,n}\) consists of reflexivity and \(a<b\) for every \(a\in A\) and \(b\in B\), with no further nontrivial comparisons. Upper sets include the empty set. Meet in \(H_{m,n}\) is intersection, and its top is \(P_{m,n}\). The rank of a nucleus means the cardinality of its *set-theoretic image* as a map on \(H_{m,n}\), not the number of supporting points. Pairs \((j_S,j_T)\) are ordered, and a nucleus may coincide with itself. The restriction \(m,n\ge2\) makes the two incomparable levels genuine; the formulas happen to extend to some singleton cases but those are not claimed as new here.

## Proof
**1. Every nucleus has exactly one support.** For a nucleus \(j\) and \(x\in P_{m,n}\), define
\[
K_x=\bigcap\{U\in\operatorname{Up}(P_{m,n}):x\in j(U)\}.
\]
Because the algebra is finite and \(j\) preserves all finite meets and top, \(K_x\) is an upper set and for every upper set \(U\),
\[
x\in j(U)\quad\Longleftrightarrow\quad K_x\subseteq U.
\]
Extensivity gives \(K_x\subseteq\uparrow x\). Isotonicity of each output upper set gives \(x\le y\Rightarrow K_y\subseteq K_x\). Since \(j^2=j\), comparison of the two equivalent predicates \(x\in j^2(U)\) and \(x\in j(U)\), valid for every upper set, yields
\[
K_x=\bigcup_{y\in K_x}K_y.
\]
Set \(S=\{s\in P_{m,n}:s\in K_s\}\). If \(s\) is a minimal point of the finite upper set \(K_x\), then the displayed union furnishes \(y\in K_x\) with \(s\in K_y\). The inclusion \(K_y\subseteq\uparrow y\) gives \(y\le s\), so minimality forces \(y=s\), and hence \(s\in S\). Thus every minimal point of \(K_x\) lies in \(S\), and every member of \(K_x\) lies above a member of \(S\cap\uparrow x\). Conversely, if \(s\in S\cap\uparrow x\), then \(s\in K_s\subseteq K_x\), since \(x\le s\). Therefore \(K_x=\uparrow(S\cap\uparrow x)\). As \(U\) is upward closed, \(K_x\subseteq U\) is equivalent to \(S\cap\uparrow x\subseteq U\), proving \(j=j_S\).

Conversely, every displayed \(j_S\) is extensive, monotone, and meet-preserving directly from its defining condition. For idempotence, observe that for \(x\in P_{m,n}\), the assertion \(x\in j_S(j_S(U))\) is equivalent to \(s\in j_S(U)\) for all \(s\in S\cap\uparrow x\), which in turn is equivalent to \(S\cap\uparrow x\subseteq U\) (every such \(s\) must lie in \(U\), and upward closure makes the reverse implication immediate). So \(j_S^2=j_S\). Finally \(S\) is recoverable from \(j_S\) by \(s\in S\Leftrightarrow s\in K_s\), establishing bijectivity.

**2. Commutation criterion and composite.** For either order of composition, membership can be tested using the following subsets:
\[
D_{S,T}(x)=\bigcup_{s\in S\cap\uparrow x}(T\cap\uparrow s),\qquad
x\in j_S(j_T(U))\ \Longleftrightarrow\ D_{S,T}(x)\subseteq U.
\]
For \(b\in B\), both \(D_{S,T}(b)\) and \(D_{T,S}(b)\) are \(\{b\}\) if \(b\in S\cap T\), and otherwise empty. For \(a\in A\), consider four mutually exclusive possibilities. If \(a\notin S\cup T\), both subsets are \(S_B\cap T_B\). If \(a\in S\cap T\), both contain \(a\); therefore their upward closures both equal \(\uparrow a\). If \(a\in S\setminus T\), then \(D_{S,T}(a)=T_B\) and \(D_{T,S}(a)=S_B\cap T_B\), so the predicates for all upper \(U\) coincide precisely when \(T_B\subseteq S_B\). The remaining case \(a\in T\setminus S\) similarly gives \(S_B\subseteq T_B\). Since an upper-set membership test depends only on the upward closure of its test subset, the announced criterion follows in both directions. Under that criterion, each such predicate agrees with the corresponding predicate for \(j_{S\cap T}\): for bottom points in exactly one support, the relevant upper support is precisely \(S_B\cap T_B\), while for shared bottom points it is equivalent to requiring the bottom point itself. Thus the common composition is \(j_{S\cap T}\).

**3. Enumerating the joint support.** Partition the choices of \((S_A,T_A)\) into equal sets, two strict-inclusion orientations, and incomparable sets. The generating polynomials recording \(|S_A\cap T_A|\) in these classes are, respectively,
\[
(1+x)^m,\quad (2+x)^m-(1+x)^m\quad\text{for each orientation},\quad
(3+x)^m-2(2+x)^m+(1+x)^m.
\]
For equal lower supports the upper supports can be arbitrary, giving \((3+y)^n\). For a strict-inclusion orientation the commutation criterion forces one specified upper support to contain the other, giving \((2+y)^n\). For incomparable lower supports it forces equality of the two upper supports, giving \((1+y)^n\). Multiplication and addition over the disjoint cases gives \(F_{m,n}\). Setting both variables to \(1\) and expanding yields \(C_{m,n}\). Expanding \(F_{m,n}\) algebraically as
\[
(1+x)^m(3+y)^n+(3+x)^m(1+y)^n+2(2+x)^m(2+y)^n
-2(1+x)^m(2+y)^n-2(2+x)^m(1+y)^n+(1+x)^m(1+y)^n
\]
shows invariance under simultaneously exchanging \(m\leftrightarrow n\) and \(x\leftrightarrow y\).

**4. Exact composite image cardinalities.** For any \(V\subseteq P_{m,n}\), the map \(j_V(U)\) depends only on \(U\cap V\). Every upper set of the induced poset \(V\) occurs as such an intersection: if \(W\) is upper in \(V\), take \(U=\uparrow_P W\). Distinct restrictions \(W\) produce distinct outputs because \(j_V(U)\cap V=U\cap V\). Thus \(|j_V[H_{m,n}]|=|\operatorname{Up}(V)|\). If \(a=|V\cap A|\) and \(b=|V\cap B|\), every upper set of \(V\) either lies entirely inside its \(b\) top points, or contains all \(b\) top points together with a nonempty subset of the \(a\) bottom points. Consequently \(|\operatorname{Up}(V)|=2^b+(2^a-1)=2^a+2^b-1\). Apply this with \(V=S\cap T\), and aggregate coefficients of \(F_{m,n}\) to obtain \(R_{m,n}\).

**5. Nonisomorphism of the exchanged algebra family.** The finite distributive lattice of upper sets determines its join-irreducible poset, which is order-isomorphic to the underlying poset up to a fixed convention of reversal. In \(P_{m,n}\), the numbers of minimal and maximal elements are \(m\) and \(n\); if \(m\ne n\), \(P_{m,n}\not\cong P_{n,m}\), and therefore \(H_{m,n}\not\cong H_{n,m}\). Yet the rank distribution above is identical, as claimed.

## Verification
Run the standalone standard-library checker with `python3 verify.py`. It constructs the actual upper-set lattice, computes all subset-indexed nuclei, composes every ordered pair, tests equality of composites directly, verifies the support criterion, checks every composite image size, and compares every bivariate profile coefficient with the formula. It checks the pairs \((m,n)\in\{(1,1),(1,2),(2,1),(2,2),(1,3),(3,1),(2,3),(3,2),(3,3)\}\), a total of \(7056\) ordered nucleus pairs. Separately it enumerates **all** inflationary idempotent meet-preserving self-maps of the upper-set lattice, without using the support representation to generate candidates, in the four smallest cases; the resulting sets equal the subset-indexed nuclei. These finite checks are not substitutes for the unrestricted proof.

For \(m=n=2\), there are \(162\) commuting ordered pairs among \(256\) pairs of nuclei. Their image-cardinality multiplicities are \(35\) at rank \(1\), \(68\) at rank \(2\), \(28\) at rank \(3\), \(18\) at rank \(4\), \(12\) at rank \(5\), and \(1\) at rank \(7\). For \((m,n)=(2,3)\) and \((3,2)\), both total counts are \(542\).

## Relationship to prior work
Marcel Erné, *Nuclear ranges in implicative semilattices* (2022), develops the general theory of nuclei and nuclear ranges in semilattices; its Lemma 3.6 records implications relating commutation to closure under composition. The present theorem uses the same classical nucleus concept but gives a complete support-level commutation criterion, a bivariate ordered-pair census, and an exact composite-image distribution for the specified height-two Heyting family; these formulas are not supplied by the cited general lemma. Jānis Cīrulis, *Modal Hilbert algebras and their triple representation* (2022, earlier manuscript 2020), also treats closure/modal operators and their general structural relationships, rather than this finite parameter-specific rank profile. Standard finite distributive-lattice duality is used only for the nonisomorphism consequence.

## Limitations
The theorem concerns finite ordinal sums of **two** antichains of widths at least two. It does not classify nuclei on arbitrary finite posets, or joint commutation of three or more nuclei. Polynomial coefficients count ordered labeled support pairs; quotienting by poset automorphisms is not addressed. Exhaustive tests are limited to the finite cases named above; the proof is general. Although targeted searches did not uncover an equivalent rank-profile formula, historical completeness and originality have not been independently certified, and an equivalent result using a different description of nuclei or binary relations may exist. 

## References
1. M. Erné, *Nuclear ranges in implicative semilattices*, Algebra Universalis **83**, article 18 (2022), first published 12 April 2022. DOI: `10.1007/s00012-022-00768-3`. Open full text: https://link.springer.com/article/10.1007/s00012-022-00768-3.
2. J. Cīrulis, *Modal Hilbert algebras and their triple representation*, Journal of Multiple-Valued Logic and Soft Computing **38** (2022), pp. 81–114; publicly circulating preprint May 2020.
3. G. Birkhoff, *Lattice Theory*, 3rd ed., American Mathematical Society, 1967 (finite distributive-lattice representation).
