# Common prime divisors of all Veronese coisotropic degrees
## Finding
Let
\[
V_{n,e}=v_e(\mathbb P^n_{\mathbb C}),
\qquad
n\ge1,
\qquad
e\ge2,
\]
be the \(e\)-th Veronese variety. Write
\[
\delta_0,\ldots,\delta_n
\]
for its polar degrees. Equivalently, these are the projective degrees of the coisotropic hypersurfaces attached to the Veronese variety.

The polar vector is
\[
\delta_i
=
\binom{n+1}{i+1}
e^i
(e-1)^{n-i},
\qquad
0\le i\le n.
\]
Its common divisor has the exact closed form
\[
\gcd(\delta_0,\ldots,\delta_n)
=
\prod_{p\mid e}p^{\nu_p(n+1)}.
\]

Thus a prime \(p\) divides every Veronese coisotropic degree if and only if
\[
p\mid e
\quad\text{and}\quad
p\mid n+1.
\]
Moreover, whenever this happens, the exact common \(p\)-adic exponent is
\[
\nu_p(n+1).
\]

Two immediate consequences are
\[
\gcd(\delta_0,\ldots,\delta_n)=1
\iff
\gcd(e,n+1)=1,
\]
and, for the quadratic Veronese,
\[
\gcd(\delta_0,\ldots,\delta_n)
=
2^{\nu_2(n+1)}.
\]

The statement is uniform over the entire polar vector: no other prime can divide all generic tangency degrees simultaneously.

## Assumptions and scope
The ground field is \(\mathbb C\), and the embedding is the standard Veronese embedding
\[
v_e:\mathbb P^n\hookrightarrow\mathbb P^N,
\qquad
N=\binom{n+e}{e}-1.
\]

The polar degrees are taken in the standard projective convention in which they are the multidegrees of the conormal variety. In this convention the first and last polar degrees are
\[
\delta_0=(n+1)(e-1)^n,
\qquad
\delta_n=e^n.
\]

The coisotropic interpretation uses the standard correspondence between polar degrees and degrees of higher associated or coisotropic hypersurfaces.

## Proof
Set
\[
N=n+1
\]
and reindex by
\[
k=i+1.
\]
Then
\[
a_k
=
\delta_{k-1}
=
\binom Nk
e^{k-1}
(e-1)^{N-k},
\qquad
1\le k\le N.
\]

Fix a prime \(p\).

First suppose
\[
p\nmid e.
\]
The final term is
\[
a_N=e^{N-1},
\]
so
\[
\nu_p(a_N)=0.
\]
Hence \(p\) does not divide the gcd of all polar degrees.

Now suppose
\[
p\mid e.
\]
Write
\[
a=\nu_p(N),
\qquad
b=\nu_p(e)\ge1.
\]
Since
\[
p\nmid e-1,
\]
we have
\[
\nu_p(a_k)
=
\nu_p\binom Nk
+
(k-1)b.
\]

Use the identity
\[
\binom Nk
=
\frac Nk
\binom{N-1}{k-1}.
\]
Because the second factor on the right is an integer,
\[
\nu_p\binom Nk
\ge
a-\nu_p(k).
\]
Also
\[
\nu_p(k)\le k-1\le(k-1)b.
\]
Therefore
\[
\nu_p(a_k)
\ge
a
\]
for every \(k\).

At
\[
k=1,
\]
we have
\[
a_1=N(e-1)^{N-1},
\]
and hence
\[
\nu_p(a_1)=a.
\]
Thus
\[
\min_{1\le k\le N}\nu_p(a_k)
=
\nu_p(N)
\]
for every prime \(p\mid e\).

Combining the two prime cases gives
\[
\gcd(\delta_0,\ldots,\delta_n)
=
\prod_{p\mid e}p^{\nu_p(n+1)}.
\]

The polar-degree formula itself follows from the standard polar-class identity
\[
\delta_i
=
\sum_{j=0}^{n-i}
(-1)^j
\binom{n-j+1}{i+1}
\int_{\mathbb P^n}
c_j(T\mathbb P^n)H^{n-j},
\]
with
\[
c_j(T\mathbb P^n)=\binom{n+1}{j}h^j
\]
and
\[
H=eh.
\]
Substitution gives
\[
\delta_i
=
\sum_{j=0}^{n-i}
(-1)^j
\binom{n-j+1}{i+1}
\binom{n+1}{j}
e^{n-j},
\]
which simplifies to the displayed closed form.

## Verification
The bundled exact checker verifies three independent finite consistency families.

First, for
\[
1\le n\le79,
\qquad
2\le e\le30,
\]
it computes every polar degree from the closed formula and confirms the gcd identity prime by prime.

Second, for
\[
1\le n\le14,
\qquad
2\le e\le10,
\]
it independently computes the polar vector from the Chern-class summation and confirms agreement with the closed formula.

Third, it verifies the identity
\[
\sum_{i=0}^{n}\delta_i
=
\frac{(2e-1)^{n+1}-(e-1)^{n+1}}{e},
\]
which agrees with the known generic Euclidean-distance degree of the Veronese variety.

These finite checks are regression evidence only. The infinite gcd theorem is proved by the valuation argument above.

## Relationship to prior work
Kohn develops the coisotropic hypersurfaces of projective varieties and explains that their degrees are precisely the polar degrees. This places the entire polar vector in a natural geometric role rather than treating its entries as unrelated intersection numbers.

Explicit formulas for the polar degrees of Segre--Veronese varieties are available in later work, and the ordinary Veronese formula above is the corresponding specialization. The quadratic case also appears in work on the geometry of semidefinite-exact quadratic optimization, where the conormal multidegree specializes to
\[
2^i\binom{n+1}{i+1}.
\]

The new contribution here is the exact arithmetic invariant of the whole polar vector: its gcd is the part of \(n+1\) supported on primes dividing the embedding degree \(e\). Searches using gcd, common-divisor, common-prime, coisotropic-degree, and Veronese polar-degree formulations did not locate this statement or an implication that already forces it.

## Limitations
The theorem concerns the gcd of the complete polar vector. It does not classify the gcd of a proper subcollection of polar degrees, which can be larger.

The proof depends on the standard projective polar-degree convention. A different indexing convention changes the order of the entries but not their gcd.

The gcd formula is a short consequence of the explicit polar vector, so there is a residual possibility that it appears in an unindexed older source even though no such statement was located in the inspected literature.

## References
Kathlén Kohn, *Coisotropic Hypersurfaces in Grassmannians*, arXiv:1607.05932, first submitted 20 July 2016.

Türkü Özlüm Çelik, Asgar Jamneshan, Guido Montúfar, Bernd Sturmfels, and Lorenzo Venturello, *Wasserstein distance to independence models*, Journal of Symbolic Computation 104 (2021), 855--873.

The standard polar-class formula for a smooth projective variety, specialized here to \(\mathbb P^n\), yields the displayed closed Veronese polar vector.
