# Complete equality cases for Thue–Morse Dyck-factor bounds
## Finding
Let \(d(n)\) be the number of distinct Dyck factors of length \(2n\) in the Thue–Morse word. The sharp bounds of Mol, Rampersad, and Shallit have the following complete equality cases.

For the upper bound,
\[
d(n)=n
\]
if and only if
\[
n\in\{1,2\}
\quad\text{or}\quad
n=3\cdot2^j
\]
for some integer \(j\ge0\).

For the global lower bound,
\[
d(n)=\frac n2
\]
if and only if
\[
n=2^j
\]
for some integer \(j\ge2\).

For the stronger odd lower bound,
\[
d(n)=\frac{n+3}{2}
\]
with \(n\) odd if and only if
\[
n\in\{3,5\}.
\]

Thus the infinite families exhibited in the source are the only infinite equality families, and the upper bound has only the two additional isolated cases \(n=1,2\).

## Assumptions and scope
A Dyck word is a binary word with equal numbers of \(0\)'s and \(1\)'s whose every prefix has at least as many \(0\)'s as \(1\)'s. The Thue–Morse word is the fixed point beginning in \(0\) of the morphism \(0\mapsto01\), \(1\mapsto10\).

The proof uses the exact recurrence relations and sharp inequalities established in the primary source:
\[
d(2m)=2d(m),
\]
\[
d(4m+3)=2d(m)+d(2m+1)+q(m),
\]
\[
d(8m+1)=2d(2m+1)+d(4m+1)-q(m),
\]
\[
d(8m+5)=2d(m)+d(2m+1)+2d(2m+2),
\]
valid for \(m\ge3\), where \(1\le q(m)\le2\). The source also proves
\[
d(n)\le n-(n\bmod2),
\]
\[
d(n)\ge\frac n2,
\]
and, for odd \(n\),
\[
d(n)\ge\frac{n+3}{2}.
\]
The DFAO defining \(q\) shows in particular that
\[
q(2^a)=2
\]
for every integer \(a\ge1\).

## Proof
First classify equality in the upper bound. The exact rank-\(7\) representation from the source gives, for \(1\le n<29\),
\[
d(n)=n
\]
exactly at
\[
n=1,2,3,6,12,24.
\]

Now let \(n\ge29\) be odd. If \(n=4m+3\), then
\[
d(n)
=
2d(m)+d(2m+1)+q(m)
\le
2m+2m+2
=
n-1.
\]
Here the stronger source bound \(d(2m+1)\le2m\) is used. If \(n=8m+1\), the source's proof of the upper bound gives directly
\[
d(n)\le n-1.
\]
If \(n=8m+5\), then
\[
d(n)
=
2d(m)+d(2m+1)+2d(2m+2)
\le
2m+2m+2(2m+2)
=
n-1.
\]
Hence no odd \(n\ge29\) attains \(d(n)=n\).

For even \(n=2m\) with \(m\ge3\),
\[
d(n)=n
\quad\Longleftrightarrow\quad
2d(m)=2m
\quad\Longleftrightarrow\quad
d(m)=m.
\]
Repeated halving therefore reduces every even equality case to the finite base range. The base value \(d(4)=2\) blocks the power-of-two branch, while \(d(3)=3\) generates
\[
3,6,12,24,\ldots.
\]
Together with the isolated base cases \(1,2\), this proves the upper equality classification.

Next consider the global lower bound. An odd \(n\) cannot satisfy
\[
d(n)=\frac n2
\]
because \(d(n)\) is an integer. For even \(n=2m\) with \(m\ge3\),
\[
d(n)=\frac n2
\quad\Longleftrightarrow\quad
2d(m)=m
\quad\Longleftrightarrow\quad
d(m)=\frac m2.
\]
In the base range the equality cases are exactly \(4,8,16\), while \(d(2)=2\ne1\). Repeated halving therefore gives precisely
\[
n=2^j,\qquad j\ge2.
\]

Finally classify equality in the stronger odd lower bound. The base range \(1\le n<29\) gives equality only at \(n=3,5\). Let \(n\ge29\) be odd.

If \(n=4m+3\), then
\[
d(n)
=
2d(m)+d(2m+1)+q(m)
\ge
m+(m+2)+q(m).
\]
Equality with \((n+3)/2=2m+3\) would require simultaneously
\[
d(m)=\frac m2
\quad\text{and}\quad
q(m)=1.
\]
The already-proved global lower equality classification forces \(m=2^a\) with \(a\ge2\), but the source DFAO gives \(q(2^a)=2\), a contradiction.

If \(n=8m+1\), the lower-bound calculation in the source yields
\[
d(n)\ge\frac{n+7}{2},
\]
so equality with \((n+3)/2\) is impossible.

If \(n=8m+5\), equality in
\[
d(n)
=
2d(m)+d(2m+1)+2d(2m+2)
\ge
\frac{n+3}{2}
\]
would force both
\[
d(m)=\frac m2
\]
and
\[
d(2m+2)=m+1.
\]
The global lower equality classification would then make both \(m\) and \(m+1\) powers of \(2\), impossible for \(m\ge3\).

Therefore the only odd equality cases are \(3\) and \(5\).

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier encodes the published rank-\(7\) linear representation exactly over rational numbers. It reproduces the source table through \(n=20\), checks every recurrence of Lemma 5.1 for \(3\le m\le5000\), and verifies from the DFA description that \(q(2^a)=2\) for \(1\le a\le39\).

It computes the complete base range \(1\le n<29\), obtaining upper equality at
\[
1,2,3,6,12,24,
\]
global lower equality at
\[
4,8,16,
\]
and odd lower equality at
\[
3,5.
\]

As an independent finite regression, it enumerates Dyck factors in Thue–Morse prefixes of lengths \(4096\) and \(32768\) and obtains the same values for every \(1\le n<29\). It also checks the final classifications for every \(n<200000\).

The infinite classification follows from the symbolic induction above; the finite computations do not substitute for that proof.

## Relationship to prior work
Mol, Rampersad, and Shallit prove the upper bound \(d(n)\le n\), exhibiting the family
\[
d(3\cdot2^j)=3\cdot2^j,
\]
and prove the lower bound \(d(n)\ge n/2\), exhibiting
\[
d(2^j)=2^{j-1}
\]
for \(j\ge2\). They also prove the stronger odd inequality \(d(n)\ge(n+3)/2\). Their paper states that these bounds are tight, but it does not classify all equality cases.

OEIS A345199 records the sequence, its regular recurrences, and the finite initial values. Its checked entry likewise gives the source and recurrences but does not state an if-and-only-if equality classification.

The present result sharpens the tightness statements to complete extremizer classifications. The proof uses the source recurrences in the reverse direction: odd inputs are shown to be strictly nonextremal beyond the finite base, while doubling propagates and only propagates the two surviving dyadic families.

## Limitations
The result classifies equality only for the three bounds proved in the source. It does not classify near-extremizers such as indices satisfying \(d(n)=n-1\) or \(d(n)=n/2+1\).

No new closed form for \(d(n)\) is claimed; the sequence remains described most naturally by its \(2\)-regular representation and recurrences.

## References
1. L. Mol, N. Rampersad, and J. Shallit, “Dyck Words, Pattern Avoidance, and Automatic Sequences,” arXiv:2301.06145v1, first public 2023-01-15; Communications in Mathematics 33 (2025), Paper 5, DOI 10.46298/cm.12695.
2. OEIS A345199, “Number of distinct length-\(2n\) blocks in the Thue–Morse sequence that are Dyck words.”
