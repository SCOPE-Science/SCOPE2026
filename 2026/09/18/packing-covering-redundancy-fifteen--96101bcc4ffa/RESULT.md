# Generalized packing--covering holds through redundancy fifteen

## Result

Let \(C\) be an \([n,k]_q\) linear code over an arbitrary finite field, let \(\rho=n-k\), and let \(d_t(C)\) and \(R_t(C)\) denote its \(t\)-th generalized Hamming weight and generalized covering radius. Then, for every code with \(\rho\le 15\) and every admissible order \(1\le t\le \min\{k,\rho\}\),
\[
 d_t(C)\le 2R_t(C)+2.
\]
Equivalently, the generalized packing--covering conjecture holds for every linear code of redundancy at most fifteen over every finite field.

Essayag and Zabokritskiy proved the universal statement through redundancy fourteen. Their reduction identifies the first binary parameter triple not excluded beyond that range as
\[
 \rho=15,\qquad t=3,\qquad R_3(C)=6,
\]
with their general dimension cap giving \(k\le78\). The argument below closes this triple and, together with the same finite reduction, closes all of redundancy fifteen.

## Reduction to one binary parameter triple

Write \(r=R_t(C)\). A counterexample must satisfy \(d_t(C)\ge 2r+3\). The established cases used by Essayag--Zabokritskiy give the following necessary conditions when \(\rho=15\):
\[
 3\le t<11,\qquad
 t+1\le r\le \left\lfloor\frac{12+t}{2}\right\rfloor,
 \qquad 3r<30,
\]
\[
 (t,r)\notin\{(3,4),(3,5),(4,5),(4,6)\},
 \qquad q<r.
\]
The last condition follows from their large-alphabet theorem. Hence \(r\le9\), and the only possible prime-power alphabets are
\[
 q\in\{2,3,4,5,7,8\}.
\]

For such a tuple put
\[
 a=15-2r+t-2,\qquad b=15-2r-1,
\]
and use their dimension cap
\[
 K(q,15,t,r)=
 \min_{a<h\le15}
 \left\lfloor
 \frac{(q^h-q^{h-a})h-b(q^h-1)}{q^{h-a}-1}
 \right\rfloor.
\]
There are 62 tuples satisfying the displayed reduction. Exact-integer evaluation gives 6 with \(K\le5t-2\), excluded by the known low-dimension case, and 55 more for which
\[
 \binom{15+K}{r}<q^{t(15-r)}.
\]
For a hypothetical counterexample, \(n\le15+K\). The generalized covering-ball inequality
\[
 V_{q^t}(n,r)\ge q^{15t},
 \qquad
 V_Q(n,r)=\sum_{i=0}^r\binom ni(Q-1)^i,
\]
together with \(V_Q(n,r)\le\binom{15+K}{r}Q^r\), contradicts the strict binomial inequality. The only tuple left is
\[
 (q,t,r)=(2,3,6),
\]
for which \(K=78\), attained at \(h=6\). The exact enumeration is reproduced by `artifacts/verify.py`.

## Closing the binary \((t,r)=(3,6)\) case

Assume for contradiction that \(C\) is binary, has redundancy \(15\), satisfies \(R_3(C)=6\), and violates the conjecture. Then
\[
 d_3(C)\ge15.
\]
Let \(H\) be a full-rank \(15\times n\) parity-check matrix and write \(k=n-15\).

### A dual fourth-weight bound

We claim
\[
 d_4(C^\perp)\ge k+2.
\]
Indeed, suppose a 4-dimensional subcode of \(C^\perp\) had support at most \(k+1\). It can be written as the row space of \(BH\) for a rank-4 matrix \(B\). At least
\[
 n-(k+1)=14
\]
columns of \(H\) then lie in \(\ker B\), whose dimension is \(11\). Those 14 columns have nullity at least three. Using
\[
 d_3(C)=\min\{|S|:|S|-\operatorname{rank}H_S\ge3\},
\]
we would obtain \(d_3(C)\le14\), a contradiction.

### Shortening to six dimensions

Choose nine coordinates whose columns of \(H\) are linearly independent. Shorten \(C^\perp\) on these coordinates and puncture the shortened positions. The resulting binary code \(E\) has dimension six and exact length
\[
 N=n-9=k+6.
\]
Every 4-dimensional subcode of \(E\) lifts to one of \(C^\perp\) with the same support, hence
\[
 d_4(E)\ge k+2=N-4.
\]

Let \(G\) be a \(6\times N\) generator matrix of \(E\). For every 2-dimensional linear subspace \(W\le\mathbb F_2^6\), the 4-dimensional annihilator \(W^\perp\) generates a subcode whose zero coordinates are precisely the columns of \(G\) lying in \(W\). Therefore every 2-space of \(\mathbb F_2^6\) contains at most four columns of \(G\), counted with multiplicity, including zero columns.

This forces
\[
 N\le64.
\]
To see it directly, let \(z\) be the multiplicity of the zero column and \(m_p\) the multiplicity of a nonzero point \(p\). If \(z=0\) and all \(m_p\le1\), then \(N\le63\). Otherwise choose a nonzero \(p\) with \(z+m_p\ge2\). Exactly 31 two-dimensional subspaces contain \(p\), and over \(\mathbb F_2\) they partition the other 62 nonzero vectors into 31 pairs. Summing the 31 inequalities saying that each such 2-space contains at most four columns gives
\[
 31(z+m_p)+\sum_{q\ne0,p}m_q\le124.
\]
Since the left side equals \(N+30(z+m_p)\), it follows that \(N\le64\).

This length estimate is also the relevant special case of the established generalized Griesmer bound: for a binary \([N,6]\) code,
\[
 N\ge d_4+\left\lceil\frac{d_4}{30}\right\rceil
       +\left\lceil\frac{d_4}{60}\right\rceil.
\]
The direct argument above is included so that the present proof does not depend on using that theorem as a black box.

Consequently
\[
 k\le58,\qquad n=k+15\le73.
\]

### Exact covering-ball contradiction

For \(q=2\), \(t=3\), \(r=6\), and \(\rho=15\), the generalized covering-ball inequality requires
\[
 V_8(n,6)\ge2^{45}.
\]
But \(n\le73\), and monotonicity in the length gives
\[
 V_8(n,6)\le V_8(73,6)
 =\sum_{i=0}^6\binom{73}{i}7^i
 =20{,}282{,}523{,}983{,}828,
\]
whereas
\[
 2^{45}=35{,}184{,}372{,}088{,}832.
\]
This is impossible. Hence the final reduced parameter triple cannot occur, completing the proof for redundancy fifteen.

## Verification

`artifacts/verify.py` uses only exact integer arithmetic. It reproduces the complete redundancy-15 finite reduction, confirms that the sole tuple left by the previous dimension-cap/binomial test is \((2,3,6)\), and checks the final covering-ball inequality. Its recorded output is in `artifacts/verification.txt`.

The proof of the special binary triple is mathematical; the script is a compact check of the finite parameter bookkeeping and arithmetic rather than evidence replacing the proof.

## Originality scope and limitations

The contribution claimed here is the extension of the universal redundancy threshold from fourteen to fifteen, obtained by closing the binary \((\rho,t,R_t)=(15,3,6)\) case explicitly identified as the first remaining triple by Essayag--Zabokritskiy and checking that no other redundancy-15 tuple survives their reductions.

The generalized Griesmer bound, generalized Hamming-weight duality, the covering-ball inequality, and the reductions from the cited work are established ingredients and are not claimed as new. In particular, the six-dimensional projective multiplicity argument above is a direct specialization of known generalized-weight geometry.

Originality is to the best of our knowledge. Searches for the generalized packing--covering conjecture together with redundancy fifteen, the exact residual triple, and synonymous generalized-covering/generalized-weight formulations found no prior statement closing redundancy fifteen. The main source was submitted on 16 September 2026 and still states redundancy fourteen as its universal theorem while identifying the above triple as remaining. A same-day or poorly indexed note could nevertheless contain an equivalent observation. No claim is made for redundancy sixteen or higher.

## References

1. Isaac Barouch Essayag and Aryeh Lev Zabokritskiy (Yohananov), *Auxiliary Codes and the Generalized Packing--Covering Conjecture*, arXiv:2609.19098v1 (2026). https://arxiv.org/abs/2609.19098
2. Sascha Kurz, Ivan Landjev, and Assia Rousseva, *Optimal Codes and Arcs for the Generalized Hamming Weights* (2026). https://epub.uni-bayreuth.de/id/eprint/8792/
