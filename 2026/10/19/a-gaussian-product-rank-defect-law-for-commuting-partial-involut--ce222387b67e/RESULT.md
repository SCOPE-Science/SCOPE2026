# A Gaussian product-rank defect law for commuting partial involutions

## Finding
Let \(\mathcal I_n\) be the symmetric inverse monoid of partial bijections on \([n]\). A *partial involution* is a member \(a\) such that \(a^{-1}=a\); it is therefore an involutive permutation of its domain, which may be empty. Write \(\mathcal P_n\) for the set of **ordered** commuting pairs of partial involutions. For \((a,b)\in\mathcal P_n\), write \(f(ab)\) and \(t(ab)\) for the numbers of fixed points and two-cycles of the partial product, and put \(D_n=n-|\operatorname{dom}(ab)|\). Then the following hold.

**Cycle-refined enumeration:** as an identity of formal power series,
\[
\sum_{n\geq0}\frac{z^n}{n!}\sum_{(a,b)\in\mathcal P_n}u^{f(ab)}v^{t(ab)}
=\exp\!\left((3+u)z+\left(1+\frac{u^2}{2}+v\right)z^2+\frac{v^2z^4}{4}\right).
\]
Consequently, writing \(a_n=|\mathcal P_n|\),
\[
\sum_{n\geq0}a_n\frac{z^n}{n!}=\exp\!\left(4z+\frac52z^2+\frac14z^4\right),
\quad a_0=1,
\]
\[
a_n=4a_{n-1}+5(n-1)a_{n-2}+(n-1)(n-2)(n-3)a_{n-4},
\]
where all negatively indexed values are zero. The first seven totals, at \(n=0,\ldots,6\), are \(1,4,21,124,817,5844,45061\).

**Prescribed-product fibers:** fix an individual partial involution \(h\in\mathcal I_n\) having \(f\) fixed points, \(t\) two-cycles, and \(m=n-f-2t\) undefined points. The number of \((a,b)\in\mathcal P_n\) with \(ab=h\) is
\[
I_fW_tH_m,
\quad I_f=\sum_{j=0}^{\lfloor f/2\rfloor}\frac{f!}{2^jj!(f-2j)!},
\]
\[
W_t=\sum_{j=0}^{\lfloor t/2\rfloor}\frac{t!2^{t-2j}}{j!(t-2j)!},
\quad H_m=m![z^m]\exp(3z+z^2).
\]
The formula is independent of the particular labels and arrangement of the cycles of \(h\).

**Asymptotic rank law:** choose \((a,b)\) uniformly from \(\mathcal P_n\). For each positive \(n\), let \(r_n\) be the unique positive solution of \(r_n^4+5r_n^2+4r_n=n\). Then
\[
\frac{D_n-(2r_n^2+3r_n)}{2r_n}\ \xrightarrow{\ \mathrm d\ }\ \mathcal N(0,1).
\]
Equivalently, since \(r_n=n^{1/4}+O(n^{-1/4})\),
\[
\frac{n-|\operatorname{dom}(ab)|-2\sqrt n-3n^{1/4}}{2n^{1/4}}
\ \xrightarrow{\ \mathrm d\ }\ \mathcal N(0,1).
\]
In particular, the typical product has rank \(n-2\sqrt n+O_{\mathbb P}(n^{1/4})\). Here \(O_{\mathbb P}\) denotes boundedness in probability. No independence of the two random factors is assumed; their distribution is uniform *conditional on commutation*.

## Assumptions and scope
The objects are finite sets and partial bijections; the theorem holds for every integer \(n\geq0\) in the exact formulas and for \(n\to\infty\) in the limit theorem. Composition follows \((ab)(x)=a(b(x))\) whenever defined. An undefined point is not a fixed point. The product of commuting partial involutions is again a partial involution. All generating functions are formal; the saddle-point proof uses the associated entire functions at positive real arguments. The natural primary classification is MSC2020 20M20.

## Proof
**1. Four invariant regions.** Let \(A=\operatorname{dom}(a)\) and \(B=\operatorname{dom}(b)\). Each factor is an involutive permutation of its domain. If \(a\) and \(b\) commute, then \(C=A\cap B\) is stable under both restrictions. Indeed, if \(x\in C\) but \(a(x)\in A\setminus B\), put \(y=a(x)\). Since \(a(y)=x\), \((ba)(y)=b(x)\) is defined, whereas \((ab)(y)\) is not: contradiction. The same argument applies to \(b\). Because \(a,b\) are bijections on their domains, their preservation of \(C\) implies preservation of the complementary regions \(A\setminus B\) and \(B\setminus A\). Thus \([n]\) splits disjointly into \(C,A\setminus B,B\setminus A,[n]\setminus(A\cup B)\). On \(C\), the restrictions are two commuting total involutions; on the next two pieces there is just one involution; on the last piece both maps are undefined. Conversely every such disjoint arrangement commutes. Their product is exactly the total involution \(a|_C b|_C\) on \(C\) and undefined outside.

**2. Indecomposable labeled blocks.** On \(C\), the commuting pair defines an action of the elementary abelian group \(C_2\times C_2\). Its transitive orbits have sizes \(1,2,4\): a singleton admits one action, a two-set admits three transitive actions, and a four-set admits \(4!/4=6\) regular actions. Among the three two-set actions, one has the product equal to the identity (two product fixed points) and two have the product a transposition. The regular action on a four-set makes the product two transpositions. Outside \(C\), there are three types of singleton (neither map defined, only \(a\) fixed, only \(b\) fixed) and two types of two-set (a transposition only of \(a\) or only of \(b\)). Hence the labeled block inventory, weighted by \(u^{f(ab)}v^{t(ab)}\), is
\[
(3+u)z+\left(1+\frac{u^2}{2}+v\right)z^2+\frac{v^2z^4}{4}.
\]
The labeled exponential formula proves the first boxed identity. Setting \(u=v=1\) and differentiating yields the recurrence. Marking undefined points with \(w\) instead yields
\[
F(z,w)=\exp\left((1+3w)z+\left(\frac32+w^2\right)z^2+\frac14z^4\right),
\quad \mathbb E[w^{D_n}]=\frac{[z^n]F(z,w)}{[z^n]F(z,1)}.
\]

**3. Each prescribed-product fiber.** Fix \(h\) as in the statement and set \(C=\operatorname{dom}(h)\). On \(C\), prescribing \(ab=h\) is equivalent to choosing an involution \(a\) in the centralizer of \(h\), then setting \(b=ah\). The centralizer is \(S_f\times(C_2\wr S_t)\). Involutions of \(S_f\) are counted by \(I_f\). In the wreath product an involution of its \(S_t\) projection with \(j\) two-cycles has \(t!/(2^j j!(t-2j)!)\) possible block permutations. The paired blocks contribute \(2^j\) compatible internal-flip choices and the fixed blocks contribute \(2^{t-2j}\), yielding \(W_t\) as stated. Outside \(C\), disjoint singleton blocks of three types and transposition blocks of two types give \(H_m=m![z^m]\exp(3z+z^2)\). These choices are independent, proving the product.

**4. Uniform saddle point and Gaussian fluctuations.** Write
\[
P_w(z)=(1+3w)z+\left(\frac32+w^2\right)z^2+\frac14z^4,
\quad P=P_1.
\]
For \(w=1\), \(r=r_n\) solves \(rP'(r)=n\) and \(B=rP'(r)+r^2P''(r)=4r+10r^2+4r^4\). Standard Cauchy-integration estimates here can be checked directly: on the circle \(|z|=r\), the maximum of \(\operatorname{Re}P(z)\) is at \(z=r\). Outside small neighborhoods of the angles \(0,\pi/2,\pi,3\pi/2\), the quartic term loses a constant multiple of \(r^4\). The neighborhoods of \(\pm\pi/2\) lose a constant multiple of \(r^2\) through the positive quadratic term, and the neighborhood of \(\pi\) loses a constant multiple of \(r\) through the positive linear term. Thus only \(\theta=0\) contributes. Inside \(|\theta|\leq r^{-2}\log r\), the Taylor expansion is \(P(re^{i\theta})-in\theta=P(r)-B\theta^2/2+O(r^4|\theta|^3)\); the remainder is \(O(r^{-2}\log^3 r)=o(1)\). The complementary arcs are exponentially negligible by the same positive-coefficient bounds. Consequently
\[
[z^n]e^{P(z)}=\frac{e^{P(r)}}{r^n\sqrt{2\pi B}}(1+o(1)).
\]
These bounds are uniform for real \(w=e^{s/(2r)}\), \(s\) in any fixed bounded interval, because the changed linear/quadratic coefficients remain positive and tend to their values at \(w=1\). Let \(r_w\) be the unique positive solution of \(r_wP_w'(r_w)=n\). Since the perturbation of the saddle equation at \(r\) is \(O(r)\), while its derivative is \(\Theta(r^3)\), the mean-value theorem gives \(r_w-r=O(r^{-2})\), uniformly on these intervals. Therefore the logarithm of the coefficient ratio satisfies
\[
\log\frac{[z^n]e^{P_w(z)}}{[z^n]e^{P(z)}}
=3r(w-1)+r^2(w^2-1)+o(1).
\]
To see the error, the first derivative of \(P_w(z)-n\log z\) vanishes at \(r_w\), so moving the saddle from \(r\) changes the exponent by \(O(r^2(r_w-r)^2)=O(r^{-2})\), while \(\log(B_w/B)=o(1)\). For \(w=e^{s/(2r)}\), subtract the proposed centering and obtain
\[
\log\mathbb E\exp\left(\frac{s(D_n-2r^2-3r)}{2r}\right)
=3r\left(e^{s/(2r)}-1\right)
+r^2\left(e^{s/r}-1\right)-\frac{s(2r^2+3r)}{2r}+o(1)
\longrightarrow \frac{s^2}{2}.
\]
The moment-generating functions thus converge to that of a standard normal on a fixed real neighborhood of zero, establishing weak convergence. Finally \(r^4=n-5r^2-4r\) implies \(r=n^{1/4}+O(n^{-1/4})\); substitution changes the centering by \(O(1)\) and scale by \(1+o(1)\), giving the simplified statement.

## Verification
The accompanying standard-library script `verify.py` constructs partial involutions independently by recursive undefined/fixed/transposed choices and composes them as literal partial maps. For every \(n\) from \(0\) through \(6\), it exhausts all ordered pairs, compares the commuting-pair total and complete product cycle profile to the block formula, and checks every individually occurring product fiber against \(I_fW_tH_m\). The output ends with `VERIFY_OK`. These exhaustive checks cover finite sizes only; the proof of the limit theorem is analytic, not computational. The exact expectations are accessible by differentiating \(F(z,w)\) at \(w=1\); in particular,
\[
\mathbb E D_n=\frac{3n a_{n-1}+2n(n-1)a_{n-2}}{a_n}.
\]

## Relationship to prior work
Lugo (2009, arXiv:0911.3604) analyzes compositions of independent, unconstrained involutions in the full symmetric group, with different orbit and cycle behavior. Araújo, Bentz and Konieczny (2012, arXiv:1205.1664) give general commutation criteria and commuting-graph results for the symmetric inverse semigroup; the basic semigroup framework and general commutation problem are established prior work. Kiefer and Leemans (2013) count commuting involution pairs in symmetric/alternating groups up to group-theoretic equivalence. The result here makes the more specific commuting **partial**-involution model explicit, resolves prescribed *partial-product* fibers, and derives the rank-defect central limit law. Neither the orbit idea nor general saddle-point methods are claimed as independently new.

## Limitations
The limit theorem describes only the product-rank defect under the indicated uniform conditional distribution; it does not claim analogous behavior for independent random partial involutions or unrestricted commuting elements of \(\mathcal I_n\). The theorem does not assert a local limit theorem, rates of convergence, or independence of other cycle statistics. The authors' comparison is not proof of absolute literature uniqueness; a previously unidentified specialized enumeration, centralizer formula, or direct asymptotic implication could overlap the claim. Independent mathematical validation has not been performed.

## References
1. M. Lugo, *The cycle structure of compositions of random involutions*, arXiv:0911.3604v1 (first public posting 2009-11-18), https://arxiv.org/abs/0911.3604.
2. J. Araújo, W. Bentz and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664v1 (2012-05-08), https://arxiv.org/abs/1205.1664.
3. A. Kiefer and D. Leemans, *On Pairs of Commuting Involutions in Sym(n) and Alt(n)*, Communications in Algebra 41 (2013), 4408–4418, https://math.uni.lu/kiefer/Publications/Involutions.pdf.
