# Maximal algebraic degree for rational Nash-welfare facility locations

## Finding

Let \(n\ge3\). A single facility is placed at \(y\in[0,1]\) for agents at rational locations \(x_1,\ldots,x_n\in[0,1]\), with utility \(u_i(y)=1-|y-x_i|\). Its Nash-welfare placement maximizes \(W(y)=\prod_{i=1}^n u_i(y)\). For every rational profile, the maximizing location is algebraic over \(\mathbb Q\) of degree at most \(n-1\). This upper bound is achieved for every \(n\ge3\) by pairwise distinct rational locations. Indeed, if \(j=\lfloor n/2\rfloor\), the profiles achieving degree exactly \(n-1\) are dense, among rational profiles, in every nonempty open sub-box of
\[
(0,1/20)^j\times(19/20,1)^{n-j}.
\]
For every such constructed profile the unique maximizing location is a root of an irreducible polynomial of degree \(n-1\) whose \(n-1\) roots are all real and simple. Thus maximum degree can persist under arbitrary rational perturbations within either two-cluster region, in the sense of density; this does not claim openness or full measure.

## Assumptions and scope

There is one facility, one unit interval, exactly \(n\ge3\) unweighted agents, rational and labeled input locations, and the normalized distance utility above. The algebraic degree of a real number means the degree of its minimal polynomial over \(\mathbb Q\). The density assertion concerns the specified open two-cluster box in the usual Euclidean topology and **does not** assert that every rational profile in the box attains maximum degree. Classical Dirichlet's theorem on primes in arithmetic progressions and Eisenstein's irreducibility criterion are used as standard number-theoretic tools.

## Proof

**1. Universal degree bound.** Between consecutive *distinct* input locations the functions \(u_i(y)\) are affine over \(\mathbb Q\); consequently \(W\) coincides with a polynomial of degree at most \(n\). If a maximizer is an endpoint of \([0,1]\) or any agent location, it is rational. Otherwise the maximizer is strictly interior to one of these cells, and is a root of a nonzero derivative polynomial over \(\mathbb Q\) of degree at most \(n-1\). That polynomial cannot be identically zero: all factors are nonzero affine factors of slope \(\pm1\), and hence their product has degree \(n\). In particular, every optimizer has algebraic degree at most \(n-1\).

**2. A fixed central gap containing the unique optimum.** Put \(j=\lfloor n/2\rfloor\), place the first \(j\) agents in \((0,1/20)\), and the others in \((19/20,1)\). On the central interval \((1/20,19/20)\), the derivative of the log welfare is
\[
G(y)=\sum_{i=j+1}^{n}\frac1{1+y-x_i}
      -\sum_{i=1}^{j}\frac1{1+x_i-y}.
\]
The function \(\log W\) is strictly concave on \((0,1)\): each \(\log(1-|y-x_i|)\) has a strictly decreasing derivative off \(x_i\) and a downward derivative jump at \(x_i\). This gives a unique global maximizer. For all allowed inputs, the bounds
\[
G(1/4)>\frac{10}3(n-j)-\frac43j>0,
\qquad
G(3/4)<\frac43(n-j)-\frac{10}3j<0
\]
hold, because \(1\le (n-j)/j\le2\) for \(n\ge3\). Therefore the unique optimizer \(y_*\) lies in \((1/4,3/4)\), strictly between the groups, independently of the precise cluster locations.

**3. Converting utilities to critical points of a real-rooted polynomial.** For left-group agents set \(r_i=1+x_i\in(1,21/20)\); for right-group agents set \(r_i=x_i-1\in(-1/20,0)\). In the central gap,
\[
W(y)=\prod_{i\le j}(r_i-y)\prod_{i>j}(y-r_i)
    =(-1)^j\prod_{i=1}^n(y-r_i).
\]
Hence \(y_*\) is a root of \(P'(Y)\), where \(P(Y)=\prod_{i=1}^n(Y-r_i)\). It remains to choose all the \(r_i\) rational and distinct, in arbitrary small prescribed intervals inside their respective groups, so that \(P'\) is irreducible of degree \(n-1\).

**4. An all-degree Eisenstein construction with prescribed real intervals.** Fix any \(n\) nonempty open real intervals \(I_i\), with \(I_i\subset(1,21/20)\) for \(i\le j\), and \(I_i\subset(-1/20,0)\) otherwise. Shrink them to make them pairwise disjoint. By Dirichlet's theorem, there exists a prime \(p\equiv1\pmod n\); necessarily \(p>n\). Let \(u_1,\ldots,u_n\) be all distinct solutions of \(u^n=1\) in \(\mathbb F_p\), in any assignment to these intervals. Thus
\[
\prod_{i=1}^n(Y-u_i)=Y^n-1\pmod p.
\]
Writing \(e_{n-1}\) for the elementary symmetric sum of degree \(n-1\), this gives \(e_{n-1}(u_1,\ldots,u_n)=0\pmod p\). Vary only the first lift from \(u_1\) to \(u_1+pt\pmod {p^2}\), leaving the other lifts fixed. Its coefficient of \(t\pmod p\) is
\[
\frac{\partial e_{n-1}}{\partial u_1}
=e_{n-2}(u_2,\ldots,u_n)
=\left(\prod_{i=2}^n u_i\right)\left(\sum_{i=2}^n u_i^{-1}\right)
=-\frac{\prod_{i=2}^n u_i}{u_1}\ne0\pmod p,
\]
since \(\sum_{i=1}^n u_i^{-1}=0\) for the complete set of \(n\)-th roots of unity (\(n\ge3\)). Thus one can choose lifts \(a_i\pmod {p^2}\) satisfying
\[
e_{n-1}(a_1,\ldots,a_n)\equiv pc\pmod {p^2},\qquad c\not\equiv0\pmod p.
\]
Now take any sufficiently large positive integer \(Q\equiv1\pmod {p^2}\). For every \(i\), choose an integer \(t_i\equiv a_i\pmod{p^2}\) with \(r_i=t_i/Q\in I_i\). Such an integer exists because the admissible grid has spacing \(p^2/Q\to0\). The numbers \(r_i\) are therefore rational, distinct, and lie in the prescribed neighborhoods.

Define the integer polynomial
\[
F(Y)=\prod_{i=1}^n(QY-t_i)=Q^nP(Y).
\]
Modulo \(p\), the conditions on \(Q\) and the residues imply \(F(Y)\equiv Y^n-1\), so \(F'(Y)\equiv nY^{n-1}\pmod p\). The leading coefficient \(nQ^n\) is not divisible by \(p\). All other coefficients are divisible by \(p\). The constant term of \(F'\) is \((-1)^{n-1}Qe_{n-1}(t_1,\ldots,t_n)\), which is divisible by \(p\) but not \(p^2\) by the choice of lifts. Eisenstein's criterion at \(p\) now proves that \(F'\) is irreducible over \(\mathbb Q\), of degree exactly \(n-1\). Its root \(y_*\) therefore has that minimal-polynomial degree.

Finally, the \(r_i\) are distinct real numbers. Rolle's theorem gives a distinct real critical point of \(F\) in each interval between consecutive ordered roots. These exhaust the \(n-1\) roots of \(F'\), proving the real-rooted assertion. As the prescribed intervals could be chosen within an arbitrarily small neighborhood of each initial cluster configuration, the required density follows.

**5. Four-agent exact witness.** Take \(Q=25001\) and transformed roots \((t_1,t_2,t_3,t_4)=(25506,25502,-496,-497)\). The corresponding agents are at
\[
(x_1,x_2,x_3,x_4)=\frac1{25001}(505,501,24505,24504).
\]
With \(F(Y)=\prod_{i=1}^4(25001Y-t_i)\), its exact derivative is
\[
\begin{aligned}
F'(Y)={}&1562750015000400004Y^3\\
&-2344734470628525045Y^2\\
&+750121981158099160Y+15833802072249820.
\end{aligned}
\]
Its coefficient reductions modulo \(5\) are \((4,0,0,0)\), in descending order, while the constant coefficient is \(20\pmod{25}\); hence it is Eisenstein at \(5\). The unique maximizing root lies between \(1/4\) and \(3/4\), numerically \(0.500129989\ldots\), and has irreducible cubic minimal polynomial.

## Verification

The standalone `verify_degree.py` uses Python standard-library exact integer and rational arithmetic, constructs representatives for every \(3\le n\le20\), and checks the modular Eisenstein conditions, interval containment, distinctness, and the opposite signs of \(G(1/4)\) and \(G(3/4)\). It separately checks the displayed four-agent integer coefficients. It passed all 19 finite witnesses when executed from this package. The finite computation is a reproducibility check, not the proof of the theorem for all \(n\); the infinite statement follows from the Dirichlet/lifting/density argument above.

## Relationship to prior work

Lam, Aziz and Walsh introduced this Nash-welfare facility objective and proved that rational inputs can force an irrational exact optimizer (their three-agent witness); they also showed uniqueness/single-peakedness and additive approximation. The earlier COMSOC-2021 workshop proceedings contain that result, and the 2023 arXiv version gives its expanded presentation. The statement here proves a stronger **every-size maximal irreducible degree** and **dense clustered rational profiles**, which is not implied by an example of quadratic irrationality, by the degree upper bound, or by an approximation algorithm. Eisenstein irreducibility and Dirichlet prime existence themselves are classical and not claimed as new.

## Limitations

This theorem applies to the precise utility \(1-|y-x_i|\), a single unweighted facility, rational input locations, and algebraic degree over \(\mathbb Q\). It says nothing about algorithmic complexity classes, degree of a general optimal welfare value, expression by radicals, generic Lebesgue-measure behavior, or multiple facilities. Density does not mean every rational profile has maximal degree. Literature comparison identifies no equivalent result in the source paper or inspected surrounding material, but publication priority in broader specialist literature is not independently certified. The COMSOC-2021 record confirms public availability during the June 7–10, 2021 workshop; exact original PDF upload time was not available, so the source date is documented as publicly available by June 10, 2021, rather than a fabricated upload timestamp.

## References

- Alexander Lam, Haris Aziz, and Toby Walsh. *Nash Welfare and Facility Location*. Proceedings of the COMSOC Workshop 2021, https://comsoc-community.org/assets/proceedings/comsoc-2021/LamEtAl.pdf ; workshop June 7–10, 2021: https://comsoc2021.net.technion.ac.il/program/ .
- Alexander Lam, Haris Aziz, and Toby Walsh. *Nash Welfare and Facility Location*, arXiv:2310.04102, first arXiv version October 6, 2023, https://arxiv.org/abs/2310.04102 .
- P. G. L. Dirichlet, theorem on primes in arithmetic progressions (classical theorem).
- G. Eisenstein, irreducibility criterion for integer polynomials (classical theorem).
