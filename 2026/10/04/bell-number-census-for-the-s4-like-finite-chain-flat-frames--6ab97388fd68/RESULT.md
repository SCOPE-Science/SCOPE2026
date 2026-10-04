# Bell-number census for the S4-like finite-chain flat frames
## Finding

Let
\[
C_n=\{0<1<\cdots<n-1\}
\]
be the \(n\)-element intuitionistic chain.

De Groot and Litak call a flat frame **upward-flat** when
\[
R\circ\leq=R.
\]
On such a frame their modal axiom
\[
\mathsf{t_{\Box}}
\]
is equivalent to reflexivity of
\[
\leq\circ R,
\]
while
\[
\mathsf{4_a}
\]
is equivalent to transitivity of \(R\).

The exact number of upward-flat relations on \(C_n\) satisfying both conditions is
\[
\boxed{B_{n+1}-B_n},
\]
where \(B_n\) is the \(n\)-th Bell number.

Thus the first values, for
\[
n=1,2,3,4,5,6,7,
\]
are
\[
1,\ 3,\ 10,\ 37,\ 151,\ 674,\ 3263.
\]

Equivalently, the finite-chain frames for the S4-like extension
\[
\mathsf{HLC}^{\mathrm{flat}}\oplus\mathsf{t_{\Box}}\oplus\mathsf{4_a}
\]
are equinumerous with set partitions of an \(n\)-element set having one distinguished block, since
\[
B_{n+1}-B_n
\]
is the total number of blocks among all set partitions of an \(n\)-element set.

The classification is explicit. Every upward-flat relation has a unique threshold vector
\[
(t_0,\ldots,t_{n-1})\in\{0,\ldots,n\}^n
\]
such that
\[
iRj
\quad\Longleftrightarrow\quad
j\ge t_i,
\]
where
\[
t_i=n
\]
means that the \(i\)-th successor row is empty.

Define the suffix minima
\[
m_i=\min_{u\ge i}t_u
\qquad(0\le i<n),
\]
and put
\[
m_n=n.
\]

Then the two frame conditions hold exactly when
\[
m_i\le i
\qquad(0\le i<n)
\]
and every threshold value
\[
q<n
\]
that occurs satisfies
\[
m_q=q.
\]

Consequently \(m\) is a nondecreasing regressive idempotent map. If its fixed-point set is
\[
F=\{0=f_0<f_1<\cdots<f_s=n\},
\]
then
\[
m_i=f_j
\qquad
(f_j\le i<f_{j+1}).
\]

For each such plateau, the last threshold is forced:
\[
t_{f_{j+1}-1}=f_j.
\]
Every earlier threshold in that plateau can be chosen independently from
\[
\{f_j,f_{j+1},\ldots,f_s\}.
\]
Hence a fixed \(F\) contributes exactly
\[
\prod_{j=0}^{s-1}
(s-j+1)^{f_{j+1}-f_j-1}
\]
relations.

Summing these contributions over all fixed-point sets gives the Bell-number difference above.

## Assumptions and scope

The theorem uses the source paper's relational semantics for flat Heyting--Lewis logic. The underlying intuitionistic order is fixed to the labelled chain \(C_n\), and the counted objects are modal relations \(R\) on that fixed carrier.

Because a finite chain has only the identity order automorphism, the labelled count is also the isomorphism-class count among frames whose intuitionistic reduct is the fixed chain.

The theorem counts the intersection of three requirements:

\[
R\circ\leq=R,
\]
\[
\leq\circ R\text{ is reflexive},
\]
and
\[
R\text{ is transitive}.
\]

It does not count all flat frames on \(C_n\), nor all finite frames validating the logic on arbitrary partial orders.

The Bell-number identity is enumerative. No direct canonical bijection with pointed set partitions is claimed here.

## Proof

### Threshold form of upward-flat relations

On a finite chain, a set is upward closed exactly when it is either empty or a suffix.

Thus
\[
R\circ\leq=R
\]
holds exactly when, for every source \(i\), there is a unique threshold
\[
t_i\in\{0,\ldots,n\}
\]
such that
\[
iRj
\quad\Longleftrightarrow\quad
j\ge t_i.
\]

The convention
\[
t_i=n
\]
encodes an empty successor row.

Put
\[
m_i=\min_{u\ge i}t_u
\]
for
\[
i<n,
\]
and
\[
m_n=n.
\]

The sequence
\[
m_0,m_1,\ldots,m_n
\]
is nondecreasing.

### The \(\mathsf{t_{\Box}}\) condition

The relation
\[
\leq\circ R
\]
is reflexive at \(i\) exactly when some
\[
u\ge i
\]
satisfies
\[
uRi.
\]
In threshold form this is
\[
t_u\le i.
\]

Hence
\[
(\leq\circ R)\text{ is reflexive}
\quad\Longleftrightarrow\quad
m_i\le i
\]
for every
\[
i<n.
\]

### The \(\mathsf{4_a}\) condition

Let
\[
t_i=q<n.
\]
Since
\[
iRj
\]
for every
\[
j\ge q,
\]
transitivity demands that every successor row beginning at such a \(j\) start no lower than \(q\):
\[
t_j\ge q
\qquad(j\ge q).
\]

Equivalently,
\[
m_q\ge q.
\]

Under the \(\mathsf{t_{\Box}}\) condition we already have
\[
m_q\le q.
\]
Therefore, when both axioms hold,
\[
m_q=q
\]
for every threshold value \(q<n\) that occurs.

Conversely, if
\[
m_i\le i
\]
for all \(i<n\) and every occurring threshold \(q<n\) satisfies
\[
m_q=q,
\]
then any chain
\[
iRj,\qquad jRk
\]
has
\[
j\ge t_i=q
\]
and
\[
t_j\ge m_q=q.
\]
Thus
\[
k\ge t_j\ge q=t_i,
\]
so
\[
iRk.
\]
Hence \(R\) is transitive.

### Idempotent suffix minima

Because the minimum defining \(m_i\) is attained, every value \(m_i<n\) occurs among the thresholds.

Therefore
\[
m_{m_i}=m_i.
\]
The value \(n\) is fixed by convention, so \(m\) is idempotent.

It is also nondecreasing and regressive:
\[
m_i\le i
\qquad(i<n).
\]

Let its fixed points be
\[
F=\{0=f_0<f_1<\cdots<f_s=n\}.
\]
The point \(0\) is fixed because
\[
m_0\le0,
\]
and \(n\) is fixed by definition.

If
\[
f_j\le i<f_{j+1},
\]
then \(m_i\) is itself a fixed point, lies at least at \(f_j\) by monotonicity, and is at most \(i<f_{j+1}\). Since there is no fixed point strictly between \(f_j\) and \(f_{j+1}\),
\[
m_i=f_j.
\]

### Recovering the thresholds from the plateaux

The suffix minima obey
\[
m_i=\min(t_i,m_{i+1}).
\]

At the final point of a plateau,
\[
i=f_{j+1}-1,
\]
we have
\[
m_i=f_j,
\qquad
m_{i+1}=f_{j+1}.
\]
Therefore
\[
t_i=f_j.
\]

At an earlier point of the same plateau,
\[
m_i=m_{i+1}=f_j,
\]
so it is necessary and sufficient that
\[
t_i\ge f_j.
\]

Any finite threshold value that occurs must be a fixed point of \(m\). Hence the allowable choices are exactly
\[
f_j,f_{j+1},\ldots,f_s=n.
\]
There are
\[
s-j+1
\]
choices at each nonfinal plateau position.

Writing
\[
d_j=f_{j+1}-f_j,
\]
the number of threshold vectors having this fixed-point set is therefore
\[
\prod_{j=0}^{s-1}(s-j+1)^{d_j-1}.
\]

### Summation and Bell numbers

For a fixed number \(s\) of plateaux, sum over all compositions
\[
d_0+\cdots+d_{s-1}=n,
\qquad
d_j\ge1.
\]

The ordinary generating function for the contribution of this fixed \(s\) is
\[
\prod_{r=2}^{s+1}
\left(
\sum_{d\ge1}r^{d-1}x^d
\right)
=
\frac{x^s}{\prod_{r=2}^{s+1}(1-rx)}.
\]

Hence the generating function for the desired counts \(a_n\) is
\[
A(x)
=
\sum_{n\ge1}a_nx^n
=
\sum_{s\ge1}
\frac{x^s}{\prod_{r=2}^{s+1}(1-rx)}.
\]

The ordinary generating function for the Bell numbers satisfies the standard formal identity
\[
B(x)
=
\sum_{n\ge0}B_nx^n
=
\sum_{k\ge0}
\frac{x^k}{\prod_{r=1}^{k}(1-rx)}.
\]

Multiplying by
\[
1-x,
\]
subtracting \(1\), and dividing by \(x\) gives
\[
\frac{(1-x)B(x)-1}{x}
=
\sum_{s\ge1}
\frac{x^s}{\prod_{r=2}^{s+1}(1-rx)}
=
A(x).
\]

But
\[
\frac{(1-x)B(x)-1}{x}
=
\sum_{n\ge1}(B_{n+1}-B_n)x^n.
\]

Therefore
\[
a_n=B_{n+1}-B_n.
\]

## Verification

The bundled checker represents every upward-flat relation on \(C_n\) by its threshold vector.

For
\[
1\le n\le6,
\]
it enumerates all
\[
(n+1)^n
\]
threshold vectors. For each vector it constructs the relation explicitly and checks, directly from relation composition, both:

\[
(\leq\circ R)\text{ is reflexive},
\]
and
\[
R\text{ is transitive}.
\]

It independently checks the suffix-minimum criterion and confirms exact agreement for every threshold vector.

The resulting counts are
\[
1,\ 3,\ 10,\ 37,\ 151,\ 674,
\]
matching
\[
B_{n+1}-B_n.
\]

Separately, through
\[
n=12,
\]
the checker evaluates the fixed-point/composition formula
\[
\sum_F
\prod_j
(s-j+1)^{f_{j+1}-f_j-1}
\]
and confirms that it equals
\[
B_{n+1}-B_n.
\]

The computation is corroborative. The arbitrary-\(n\) result follows from the threshold and generating-function proof.

## Relationship to prior work

De Groot and Litak introduce flat and upward-flat frames for Heyting--Lewis logic and prove that upward-flat replacement preserves the complex algebra. Their correspondence table identifies
\[
\mathsf{t_{\Box}}
\]
with reflexivity of
\[
\leq\circ R
\]
and
\[
\mathsf{4_a}
\]
with transitivity of \(R\). They also prove the finite model property for the extension containing both axioms.

The checked paper does not specialize those frame conditions to finite chains, enumerate the resulting relations, or connect the finite-chain count to Bell numbers.

The present result supplies an exact finite search-space description for the simplest linearly ordered intuitionistic reducts of that S4-like extension. The threshold normal form converts the two modal frame conditions into a regressive idempotent suffix-minimum structure, and the remaining independent threshold choices yield the Bell-number difference.

Targeted searches for finite-chain flat-frame counts, Bell-number formulas, upward-flat transitive chain relations, and the joint
\[
\mathsf{t_{\Box}}+\mathsf{4_a}
\]
chain case did not locate an equivalent result.

## Limitations

The count is specific to linearly ordered intuitionistic reducts. General finite posets need not admit a one-threshold-per-row description.

The theorem assumes upward-flatness. A flat frame can first be replaced by its upward-flat saturation without changing the complex algebra, but the number of raw unsaturated relations is a different enumeration problem.

No claim is made that the Bell-number count yields an optimal decision procedure for the full logic, or that the distinguished-block interpretation extends to a natural frame-level bijection.

The exact finite-chain count may have an equivalent formulation in enumerative relation theory under terminology unrelated to Heyting--Lewis semantics; no such formulation was located in the checked searches.

## References

[1] Jim de Groot and Tadeusz Litak, “Relational Semantics for Flat Heyting-Lewis Logic,” arXiv:2603.28402, first posted 30 March 2026; *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 445–463. DOI:10.4204/EPTCS.447.25.

[2] Eric Temple Bell, “Exponential Numbers,” *The American Mathematical Monthly* 41(7) (1934), 411–419.
