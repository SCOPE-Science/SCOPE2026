# Signed-binary closures improve EF depth for prime cyclic groups
## Finding
Work in the relational group language \(L_G=(R,e)\) used by Gomaa, where \(R(x,y,z)\) means \(x+y=z\) and \(e\) names the identity. Let \(p<q\) be primes and choose \(n\ge1\) with
\[
2^n<p<2^{n+1}.
\]
Write \(s_2(m)\) for the number of \(1\)-bits in the binary expansion of \(m\), and define
\[
h(p)=\min\{s_2(p-2^n),\ s_2(2^{n+1}-p)\}.
\]
Then Spoiler wins the Ehrenfeucht--Fraisse game on \(\mathbb Z_p\) and \(\mathbb Z_q\) in at most
\[
n+h(p)\le n+\lceil n/2\rceil
\]
rounds, while playing every move in \(\mathbb Z_p\). Consequently there is an existential first-order sentence in \(L_G\) of quantifier rank at most \(n+h(p)\) that distinguishes the two groups.

Gomaa proved that every distinguishing sentence has quantifier rank at least \(n+1\). Therefore the exact distinguishing quantifier rank is \(n+1\) whenever \(p=2^n+1\) or \(p=2^{n+1}-1\) is prime. In particular, the prime-order case of the published \(2n\) upper bound admits the uniform improvement \(n+\lceil n/2\rceil\).

## Assumptions and scope
The language is exactly Gomaa's ternary-relation presentation of a cyclic group, not the usual functional language. Thus a long integer multiple cannot be written as one atomic term; intermediate selected elements are needed to expose repeated addition.

The theorem concerns pairs of distinct prime-order cyclic groups with \(p<q\). It does not claim the same bound for arbitrary composite cyclic groups, where a tuple forcing \(p\)-torsion can have copies inside proper subgroups and additional subgroup-exclusion constraints are needed.

## Proof
Put \(a=p-2^n\) and \(b=2^{n+1}-p=2^n-a\). First select the \(n+1\) elements
\[
x_i=2^i\pmod p,\qquad 0\le i\le n.
\]
They are distinct and nonzero because \(2^n<p\). Their atomic diagram contains
\[
R(x_i,x_i,x_{i+1})\qquad(0\le i<n).
\]

Suppose first that \(s_2(a)\le s_2(b)\), and let \(w=s_2(a)\). If \(a=2^{j_1}+\cdots+2^{j_w}\), build the running sum \(a\) from the already selected \(x_{j_r}\). For \(w=1\) no new point is needed. For \(w\ge2\), select \(w-1\) new points whose integer representatives are the successive partial sums of these distinct powers of two. Every new relation is of the form \(R(u,v,z)\), and the final relation is
\[
R(x_n,z,e),
\]
where \(z\) represents \(a\). These points are all nonzero and distinct: every partial sum is strictly between \(0\) and \(2^n\) and has at least two nonzero binary digits. The total number of selected points is \(n+w\).

If instead \(s_2(b)<s_2(a)\), build \(b\) from the lower-power points in the same way. The closing atomic relation is now
\[
R(x_n,x_n,z),
\]
because \(2^{n+1}\equiv b\pmod p\). Again the tuple has length \(n+s_2(b)\).

Consider any response tuple in \(\mathbb Z_q\) that preserves the displayed atomic relations, and let \(y\) be the response to \(x_0\). The doubling relations force the responses to \(x_i\) to be \(2^iy\), and the running-sum relations force the auxiliary responses to be the corresponding integer multiples of \(y\). In the first construction the closing relation gives \(py=0\); in the second it gives \(2^{n+1}y=by\), hence again \(py=0\). Since \(q\) is prime and \(q\ne p\), multiplication by \(p\) is injective on \(\mathbb Z_q\), so \(y=0\). But \(x_0\ne e\), and equality to the distinguished identity is atomic, so a partial isomorphism cannot send \(x_0\) to \(0\). Thus Duplicator must lose by the last selected point. All Spoiler moves are on the \(\mathbb Z_p\) side, so the corresponding distinguishing sentence may be chosen existential.

It remains to bound \(h(p)\). More generally, for \(1\le a<2^n\), let \(t=v_2(a)\) and write \(a=2^tc\) with \(c\) odd. Setting \(m=n-t\), one has
\[
s_2(c)+s_2(2^m-c)=m+1.
\]
Indeed, \(2^m-c=(2^m-1)-(c-1)\), so its \(m\)-bit word is the bitwise complement of \(c-1\); because \(c\) is odd, \(s_2(c-1)=s_2(c)-1\). Multiplication by \(2^t\) does not change binary weight, hence
\[
s_2(a)+s_2(2^n-a)=n-t+1.
\]
Therefore
\[
\min\{s_2(a),s_2(2^n-a)\}\le \left\lfloor\frac{n-t+1}{2}\right\rfloor\le\lceil n/2\rceil.
\]
This proves the uniform upper bound.

Finally, Gomaa's Theorem 3.3 gives the lower bound \(n+1\) for prime \(p<q\) in this interval. If \(p=2^n+1\), then \(s_2(a)=1\); if \(p=2^{n+1}-1\), then \(s_2(b)=1\). The upper and lower bounds then coincide.

## Verification
The accompanying `verify.py` checks the binary-weight identity and constructs both closure types for every odd prime \(p<20000\). It verifies that all selected representatives are distinct and nonzero, that the claimed closing congruence holds, that the tuple length is \(n+h(p)\), and that \(h(p)\le\lceil n/2\rceil\). It also checks the exact-bound examples \(p=7,17,31,127\). The script returns a single `VERIFY_OK` line.

The computation is only a finite sanity check. The theorem follows from the symbolic argument above.

## Relationship to prior work
Gomaa's dissertation and later paper study precisely this relational language and prove, for primes \(2^n<p<2^{n+1}<q\) in the relevant notation, a lower bound of \(n+1\) rounds and an upper bound of \(2n\) rounds. The dissertation's open-problem section explicitly asks whether the \(n/2n\) quantifier-rank bounds for residue-class and dihedral groups can be improved and states a belief that the upper bound is optimal.

The present construction reuses the mandatory doubling chain but closes it using whichever of the two binary gaps to the adjacent powers of two has smaller Hamming weight. Searches of the primary source, the published-finding corpus finding database, and public web sources found no statement of the \(n+h(p)\) bound, the \(n+\lceil n/2\rceil\) uniform consequence, or the exact Mersenne/Fermat-prime cases.

## Limitations
This does not settle the worst-case optimum for arbitrary cyclic groups, nor does it improve the published lower bound beyond \(n+1\). It also does not retain Gomaa's separate five-variable guarantee; only quantifier rank and existentiality are claimed here.

Priority risk remains for unindexed notes or later literature that may have revisited Gomaa's 2007--2010 bounds without using the same terminology.

## References
1. Walid Gomaa, *Model Theory and Complexity Theory*, PhD dissertation, University of Maryland, public repository date 2007-07-06, especially Chapter 3 and Section 3.9. Handle: http://hdl.handle.net/1903/7227
2. Walid Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20(8), 2010, DOI: 10.1142/S0218196710006047.
