# Forbidden nilpotency-index gaps for three-step lifts of a regular nilpotent matrix

## Finding

Let \(q\) be any prime power and \(n\ge1\). Set \(R_q=\mathbb F_q[\varepsilon]/(\varepsilon^3)\), and let \(J_n\) be a single nilpotent Jordan block over \(\mathbb F_q\). Among the \(T=q^{2n^2}\) matrices \(X=J_n+\varepsilon C+\varepsilon^2D\), where \(C,D\in M_n(\mathbb F_q)\), let \(\kappa(X)\) be the least positive integer such that \(X^{\kappa(X)}=0\), and put \(c=\lceil n/2\rceil\). The attainable nilpotency indices are exactly \(\{n,n+1,\ldots,2n\}\cup\{3n-2r:0\le r<c\}\). Their complete frequencies, with all other frequencies zero, are:
\[
\#\{X:\kappa(X)=3n-2r\}=(q-1)q^{2n^2-r-1}\quad(0\le r<c),
\]
\[
\#\{X:\kappa(X)=2n-t\}=
\begin{cases}
(q-1)q^{2n^2-c-t-1},&0\le t<c,\\
q^{2n^2-2t}-q^{2n^2-2t-2},&c\le t<n,\\
q^{2n^2-2n},&t=n.
\end{cases}
\]
The two displayed index families are disjoint. In particular, for \(n\ge2\), every other index strictly between \(2n\) and \(3n\) is forbidden; the maximal nilpotency index \(3n\) occurs for a proportion \(1-q^{-1}\) of all lifts.

## Assumptions and scope

All rings are unital and commutative, and all matrices and powers are evaluated over \(R_q=\mathbb F_q[\varepsilon]/(\varepsilon^3)\). The characteristic of \(\mathbb F_q\) is arbitrary. Here \(J_n\) has entries one immediately above the diagonal and zero elsewhere. Its lift \(X\) need not commute with \(J_n\). Nilpotency index refers to the least positive annihilating power, not to ordinary matrix rank. The set of lifts has cardinality \(q^{2n^2}\).

For a polynomial \(g(T)\) of degree less than \(n\), define \(v(g)\) to be the smallest exponent with nonzero coefficient, or \(n\) when \(g=0\). We distinguish the indeterminate \(T\) used in the proof from the total lift count \(q^{2n^2}\).

## Proof

**1. Cyclic companion reduction and uniform fibers.** Choose a cyclic vector \(v\) for the reduction \(J_n\), and use the same vector over \(R_q\). The determinant of the columns \(v,Xv,\ldots,X^{n-1}v\) is nonzero modulo \(\varepsilon\), hence is a unit. Therefore every lift is similar over \(R_q\) to a companion matrix with monic characteristic polynomial
\[
f(T)=T^n-\varepsilon g(T)-\varepsilon^2h(T),\qquad \deg g,\deg h<n.
\]
Consequently \(X\) is multiplication by \(T\) on the free \(R_q\)-module \(S=R_q[T]/(f)\).

Expand the determinant at \(J_n\). The coefficient of \(\varepsilon\) is the linear map
\[
L(C)(T)=-\operatorname{tr}(\operatorname{adj}(TI-J_n)C)
=-\sum_{i=0}^{n-1}T^{n-1-i}\operatorname{tr}(J_n^i C).
\]
The functional \(\operatorname{tr}(J_n^i C)\) is the sum of entries on the \(i\)-th lower subdiagonal of \(C\), and these \(n\) disjoint sums are linearly independent over every field. Thus \(L\colon M_n(\mathbb F_q)\longrightarrow\mathbb F_q[T]_{<n}\) is surjective. The quadratic part of the determinant has the form \(L(D)+Q(C)\), where \(Q\) depends only on \(C\). For each prescribed pair \((g,h)\), the number of \((C,D)\) is exactly
\[
q^{n^2-n}q^{n^2-n}=q^{2n^2-2n}.
\]
So \(g\) and \(h\) are independent uniform polynomials of degree less than \(n\).

**2. Powers in the cyclic quotient.** The defining relation yields
\[
T^n=\varepsilon g+\varepsilon^2h,\qquad
T^{2n}=\varepsilon^2g^2,\qquad T^{3n}=0.
\]
Products on the right are understood in \(S\), and in an expression multiplied by \(\varepsilon^2\), coefficients are reduced modulo \(T^n\). Put \(r=v(g)\).

When \(2r<n\), the element \(\varepsilon^2T^jg^2\) is nonzero exactly for \(0\le j<n-2r\). In particular \(T^{3n-2r-1}\ne0\) but \(T^{3n-2r}=0\), giving \(\kappa=3n-2r\), independently of \(h\).

When \(2r\ge n\), the polynomial \(g^2\) is divisible by \(T^n\). Define
\[
h^\prime=h+g^2/T^n\pmod{T^n},\qquad s=v(h^\prime).
\]
The map \(h\mapsto h^\prime\) is a translation and therefore preserves uniformity conditional on \(g\). For \(0\le j<n\), the \(\varepsilon\)-term of \(T^{n+j}\) is nonzero whenever \(j+r<n\); once \(j+r\ge n\), reducing this term by \(T^n=\varepsilon g+\varepsilon^2h\) leaves
\[
T^{n+j}=\varepsilon^2T^jh^\prime.
\]
The last nonzero power is thus \(T^{2n-\min(r,s)-1}\), and
\[
\kappa=2n-\min(r,s).
\]
These two cases account for every pair \((g,h)\), including \(g=0\), and give disjoint high and low index ranges.

**3. Count valuations.** For a uniform \(g\in\mathbb F_q[T]_{<n}\),
\[
\Pr(v(g)=r)=(q-1)q^{-r-1}\quad(0\le r<n),\qquad
\Pr(v(g)\ge a)=q^{-a}\quad(0\le a\le n).
\]
Write \(c=\lceil n/2\rceil\). The case \(2r<n\) means exactly \(0\le r<c\), yielding \((q-1)q^{-r-1}\) for its index. Otherwise \(r\ge c\), and the independent uniform translated polynomial \(h^\prime\) has valuation \(s\). For \(t<c\),
\[
\Pr(r\ge c,\min(r,s)=t)=q^{-c}(q-1)q^{-t-1}.
\]
For \(c\le t<n\),
\[
\Pr(\min(r,s)=t)=q^{-2t}-q^{-2t-2},
\]
and for \(t=n\) this probability is \(q^{-2n}\). Multiplication by \(q^{2n^2}\) gives exactly the counts in the finding; they sum to \(q^{2n^2}\) by the partition into these exhaustive cases. Every displayed count is strictly positive. This also verifies the endpoint \(n=1\).

## Verification

The attached standalone `verify_lifts_length3.py` uses only Python's standard library. Its `enumeration` routine independently computes powers of every lift as a \(3n\)-dimensional matrix over the residue field, exhausting \((n,q)=(1,2),(2,2),(2,3)\); in particular the \((2,2)\) index frequencies are \(16,48,64,128\) at indices \(2,3,4,6\), and index \(5\) does not occur. Its separate `polynomial` routine enumerates all companion polynomial pairs for \((2,5),(3,2),(3,3),(4,2),(5,2)\). Further checks over \(\mathbb F_4\) use explicitly implemented field arithmetic for \(n=2,3\). The script prints `VERIFY_OK` and `VERIFY_GF4_OK`. These finite tests are checks, not the proof for arbitrary \(n\) or \(q\).

## Relationship to prior work

Prasad, Singla and Spallone (2012 preprint, 2015 journal) study similarity and nilpotent lifting over length-two local rings, including their cyclic case; their ring has \(\varepsilon^2=0\), so it cannot exhibit the new \(\varepsilon^2\)-correction or the length-three index gaps. Avni, Onn, Prasad and Vaserstein (2007 preprint, 2009 journal) classify similarity classes of \(3\times3\) matrices over principal local rings of general length, but their results do not state the index frequencies for all matrix sizes. Earlier work on nilpotent commuting matrices likewise concerns matrices over fields. A published enumeration over dual numbers gives all indices from \(n\) through \(2n\); the present length-three result is not its direct specialization and is characterized by a forbidden-index phenomenon.

## Limitations

The theorem concerns lifts of one *regular* nilpotent block over the equicharacteristic chain ring \(\mathbb F_q[\varepsilon]/(\varepsilon^3)\), not lifts of general nilpotent Jordan types, general ramified chain rings, or length exceeding three. The finite checks do not independently validate the general proof. A broader theorem about cyclic matrices over Artinian chain rings could imply the same frequency law; no such exact implication was established from the sources inspected.

## References

1. A. Prasad, P. Singla, and S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157 (first public version 2012-12-26), Sections 6 and 8.
2. N. Avni, U. Onn, A. Prasad, and L. Vaserstein, *Similarity classes of 3x3 matrices over a local principal ideal ring*, arXiv:0708.1608 (first public version 2007-08-12), Sections 1–3.
3. P. Oblak, *The upper bound for the index of nilpotency for a matrix commuting with a given nilpotent matrix*, arXiv:math/0701561 (first public version 2007-01-19).
