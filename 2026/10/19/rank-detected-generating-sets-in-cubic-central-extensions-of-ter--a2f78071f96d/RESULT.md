# Rank-detected generating sets in cubic central extensions of ternary midpoint quandles

## Finding

Let \(d\geq3\), \(V=\mathbb F_3^d\), let \(B:V\times V\to\mathbb F_3\) be any alternating bilinear form, and let \(L:V\to\mathbb F_3\) be linear. Define the alternating trilinear form
\[
T(a,b,c)=B(a,b)L(c)+B(b,c)L(a)+B(c,a)L(b).
\]
Assume \(T\ne0\). On the \(3^{d+1}\)-point set \(Q=V\times\mathbb F_3\), define
\[
(u,s)\star(v,t)=\big(-u-v,\,-s-t+B(u,v)(L(u)-L(v))\big).
\]
**Theorem.** This operation is a commutative, Latin, involutory, nonmedial quandle. For every nonempty subset \(S\subseteq Q\),
\[
\langle S\rangle_\star=Q\quad\Longleftrightarrow\quad
\operatorname{aff}_{\mathbb F_3}\{u:(u,s)\in S\}=V.
\]
Consequently, for every integer \(k\geq d+1\), the number of **ordered** generating \(k\)-tuples (repetitions permitted) is
\[
G_k(Q)=3^{d+k}\prod_{j=0}^{d-1}(3^{k-1}-3^j),
\qquad
\Pr(\text{a uniform ordered }k\text{-tuple generates})
=\prod_{j=0}^{d-1}(1-3^{j-k+1}).
\]
For \(1\leq k\leq d\), \(G_k(Q)=0\); thus the minimum number of generators is exactly \(d+1\). Both the generation criterion and probability are independent of the particular choice of \(B,L\) satisfying \(T\ne0\). The nonmediality criterion itself is sharp: if \(T=0\), the same construction is medial.

For the canonical case \(d=3\), \(B(u,v)=u_1v_2-u_2v_1\), and \(L(u)=u_3\), the four-generator probability is \(416/729\), and there are exactly \(24,564,384\) ordered generating quadruples among the \(81^4\) quadruples of this quandle of order \(81\).

## Assumptions and scope

Everything takes place over the prime field \(\mathbb F_3\). The symbol \(\operatorname{aff}_{\mathbb F_3}\) denotes affine span in \(V\). A quandle is an idempotent right-self-distributive magma whose right translations are bijections. It is *Latin* when its left translations are also bijections; *medial* means \((x\star y)\star(z\star w)=(x\star z)\star(y\star w)\) for all four inputs. A generating tuple refers to closure under the quandle operation, not a vector-space spanning tuple or a list of abstract generators. For \(d>3\), there are nonzero examples, e.g., choosing \(B(u,v)=u_1v_2-u_2v_1\) and \(L(u)=u_3\).

## Proof

Put \(\phi(u,v)=B(u,v)(L(u)-L(v))\). By alternation of \(B\), \(\phi(v,u)=\phi(u,v)\) and \(\phi(u,u)=0\). Since \(-2=1\) in \(\mathbb F_3\), \(\star\) is idempotent and commutative. For fixed \((v,t)\), the map \((u,s)\mapsto(-u-v,-s-t+\phi(u,v))\) is bijective: recover \(u\) from its first component and then \(s\) from its second. Commutativity gives left bijectivity. Moreover, \(\phi(-u-v,v)=\phi(u,v)\), so every right translation is an involution.

For self-distributivity, let \(A=B(u,v)\), \(C=B(u,w)\), \(D=B(v,w)\), and \(a=L(u)\), \(b=L(v)\), \(c=L(w)\). The difference between the central coordinates of \(((u,s)\star(v,t))\star(w,r)\) and \(((u,s)\star(w,r))\star((v,t)\star(w,r))\) is
\[
\phi(-u-v,w)-\phi(u,v)-\phi(-u-w,-v-w)+\phi(u,w)+\phi(v,w)
=3(Ca+Db)=0.
\]
The base coordinates also agree, proving the quandle axioms.

Direct expansion, again using only bilinearity of \(B\) and linearity of \(L\), gives the **medial-defect identity**
\[
\begin{aligned}
&\operatorname{cen}\big(((u,s)\star(v,t))\star((w,r)\star(z,h))\big)\\
&\qquad-\operatorname{cen}\big(((u,s)\star(w,r))\star((v,t)\star(z,h))\big)\\
&=-T(v-u,w-u,z-u).
\end{aligned}
\]
The base coordinates of the two terms are equal. It follows that mediality is equivalent to \(T=0\). Under the theorem's hypothesis \(T\ne0\), four projected points with a nonzero \(T\)-value give an explicit medial-law failure.

Let \(H=\langle S\rangle_\star\) and let \(\pi:Q\to V\) be projection. The base operation is \(u\bullet v=-u-v\). Any affine subspace is closed under \(\bullet\). Conversely, choose a projected seed \(u_0\), translate to coordinates \(u-u_0\), and note that \(0\bullet x=-x\), \(0\bullet(x\bullet y)=x+y\). Thus closure of the projected seeds under \(\bullet\) equals precisely their affine span.

If that affine span is proper, \(H\ne Q\). Suppose instead it is all of \(V\). Differences of the projected seeds from a fixed seed span \(V\). Because \(T\ne0\) and is trilinear, there are three such differences \(a,b,c\) with \(T(a,b,c)\ne0\). The corresponding four seeds produce, through the two medial words, two members of \(H\) with the same base \(p\) but distinct central coordinates. Their product has the same base (since \(-2p=p\)) and the third central coordinate (since \(\phi(p,p)=0\)), so \(H\) contains all three elements of the fibre \(\pi^{-1}(p)\). As \(\pi(H)=V\), for each \(q\in V\) choose \((v,t)\in H\) with \(v=-p-q\). Multiplying the three elements of \(\pi^{-1}(p)\) by \((v,t)\) yields all three elements of \(\pi^{-1}(q)\), because the central coefficient is \(-s-t+\phi(p,v)\). Therefore \(H=Q\).

Finally, choose the first projected point arbitrarily (\(3^d\) choices). The differences of the other \(k-1\) projected points form a spanning ordered list of \(k-1\) vectors in \(\mathbb F_3^d\). The rank-\(d\) matrix count is \(\prod_{j=0}^{d-1}(3^{k-1}-3^j)\). Each projected \(k\)-tuple admits \(3^k\) central-coordinate lifts. Multiplication gives \(G_k(Q)\), and division by \(|Q|^k=3^{(d+1)k}\) gives the probability. For \(k\le d\), affine spanning is impossible.

## Verification

The standalone `verify.py` uses exact arithmetic modulo three. It exhaustively checks the quandle axioms for all \(81\) elements in the canonical \(d=3\) model, including all \(81^3=531,441\) self-distributivity triples. It independently enumerates all \(27^4=531,441\) projected quadruples, recovering \(303,264\) affine-independent projected quadruples and hence \(24,564,384\) ordered quandle-generating quadruples after multiplying by \(3^4\). It constructs the closure of an explicit four-element generating set, tests the medial witness, checks the cubic identities on randomized forms in dimensions three through five, and tests additional randomly chosen generating tuples. The general theorem is algebraic; finite tests do not replace the proof.

To reproduce: `python verify.py` (Python 3, standard library only). Expected final line begins `VERIFY_OK:`.

## Relationship to prior work

Kepka and Němec (1981) classified the smallest nonmedial commutative distributive quasigroups, of order \(81\). Their classification provides context for the canonical \(d=3\) member here. Ta's openly available January 20, 2026 exposition and February 9, 2026 preprint discuss the same classical order-\(81\) phenomenon and contain an explicit four-point nonmedial witness. Accordingly **the existence of a four-generated nonmedial commutative quandle is not claimed as new**: it already follows from the known witness. The finding here is the all-dimension **if-and-only-if generation criterion** and exact **every-arity ordered generating-tuple law** for the cubic central-extension family. The earlier papers address structure and classification, rather than these random-generation invariants. Further literature may express an equivalent criterion in terms of generating a nonassociative commutative Moufang loop or a Frattini quotient.

## Limitations

The theorem concerns the explicitly defined characteristic-three central extensions with decomposable nonzero alternating three-form \(T=B\wedge L\); it does not classify all distributive quasigroups or all Hall triple systems. Different pairs \((B,L)\) can represent isomorphic quandles, and no classification of their isomorphism types is asserted. The generator law depends on the nonzero-form assumption; the medial case \(T=0\) can have different generation behavior. Although primary sources were inspected, equivalently phrased generator counts in older specialized literature cannot be ruled out categorically. No independent audit has been performed.

## References

1. Lực Ta, *Structure theory of commutative quandles and medial Latin quandles*, publicly dated January 20, 2026, https://luc-ta.github.io/blog/2026/commutative-quandles/ (especially §§3.1 and 6).
2. Lực Ta, *On medial Latin quandles and affine modules*, arXiv:2602.08875v1, February 9, 2026; *Canadian Mathematical Bulletin* (2026), DOI: 10.4153/S0008439526102306, especially §§3 and 6.
3. T. Kepka and P. Němec, *Commutative Moufang loops and distributive groupoids of small orders*, *Czechoslovak Mathematical Journal* **31** (1981), 633–669, DOI: 10.21136/CMJ.1981.101778 (particularly §14).
4. P. Jedlička et al., *Distributive and trimedial quasigroups of order 243*, *Discrete Mathematics* (2017), DOI: 10.1016/j.disc.2016.08.022 (classification and historical constructions).
