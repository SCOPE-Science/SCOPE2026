# Frobenius boundary obstructions for cubic-to-Engel probability comparison

## Finding

For every integer \(m\ge3\) divisible by \(3\), **any nondecreasing universal comparison function** \(f:(0,1]\to(0,1]\) satisfying
\[
\Pr_{x,y\in G}([[x,y],y]=1)\ge f\bigl(\Pr_{x\in G}(x^3=1)\bigr)
\]
for every finite group \(G\) necessarily satisfies
\[
\boxed{f(2/m)\le 1/m.}
\]
In particular \(f(2/3)\le1/3\). The obstruction is witnessed asymptotically by an explicit infinite family of finite Frobenius groups. It is an upper restriction on all possible universal bounds, **not** a claim that the upper restriction is attained by some valid universal lower-bound function.

## Assumptions and scope

We use \([x,y]=x^{-1}y^{-1}xy\) and \([x,y,y]=[[x,y],y]\). For a finite group, probabilities use independent uniform samples. Let \(A\ne0\) be a finite abelian group of order \(a\) and let \(C_m=\langle c\rangle\) act on \(A\) by automorphisms, where every nonidentity element of \(C_m\) fixes only the zero of \(A\). Such a semidirect product \(G=A\rtimes C_m\) is a Frobenius group. Here \(3\mid m\) and \(m\ge3\); no assumption that \(A\) is a vector space is required. The special scalar construction takes the additive group of \(\mathbb F_q\) and a subgroup of order \(m\) in its multiplicative group.

## Proof

**Step 1: the 2-Engel probability.** Write \(x=(u,r)\) and \(y=(v,s)\), with \(u,v\in A\) and \(r,s\in C_m\). Since \(C_m\) is abelian, \([x,y]\in A\). If \(s=1\), then \([x,y]\) and \(y\) are both in the abelian kernel, and \([x,y,y]=1\) for every \(x\). If \(s\ne1\), the automorphism \(1-s\) of the additive group \(A\) is injective, hence bijective. Thus \([[x,y],y]=1\) if and only if \([x,y]=1\). Comparing the two possible products \(xy=(u+rv,rs)\) and \(yx=(v+su,sr)\), commutativity is equivalent to \((1-s)u=(1-r)v\). For each fixed \(r,s\) with \(s\ne1\) and each \(v\in A\), the bijectivity of \(1-s\) gives exactly one \(u\). Therefore the conditional 2-Engel probability is \(1\) when \(s=1\), and \(1/a\) otherwise. Averaging over the \(m\) equally likely values of \(s\),
\[
\Pr_G([x,y,y]=1)=\frac1m+\frac{m-1}{ma}=\frac{a+m-1}{am}.
\]

**Step 2: the cube probability.** A nonidentity element of order \(3\) in the complement acts without nonzero fixed points on \(A\). In particular \(A\) has no elements of order \(3\): otherwise the nonzero characteristic subgroup \(A[3]\), viewed as a vector space over \(\mathbb F_3\), would admit a fixed-point-free automorphism of order \(3\), impossible because its minimal polynomial divides \((T-1)^3\). Hence exactly one kernel element satisfies \(u^3=1\). An element \((u,s)\) with \(s^3=1\ne s\) has cube \((u+su+s^2u,1)\). Since \((1-s)(1+s+s^2)=1-s^3=0\) and \(1-s\) is bijective, this cube is the identity for *every* \(u\in A\). There are exactly two nonidentity elements of order \(3\) in \(C_m\), and no element with \(s^3\ne1\) can have cube one. Exactly \(1+2a\) group elements have cube one, so
\[
\Pr_G(x^3=1)=\frac{2a+1}{am}.
\]

**Step 3: a boundary for universal comparison.** Fix an arbitrary multiple \(m\) of \(3\). Choose a prime \(p\) not dividing \(m\) and set \(q_k=p^{k\varphi(m)}\) for positive integers \(k\). Euler's theorem gives \(m\mid q_k-1\), so \(\mathbb F_{q_k}^{\times}\) has a cyclic subgroup \(C_m\). Its scalar action on \((\mathbb F_{q_k},+)\) is fixed-point-free outside the identity. For the resulting groups \(G_k\),
\[
\Pr_{G_k}(x^3=1)=\frac2m+\frac{1}{mq_k}>\frac2m,
\qquad
\Pr_{G_k}([x,y,y]=1)=\frac1m+\frac{m-1}{mq_k}\longrightarrow\frac1m.
\]
If \(f\) is nondecreasing and satisfies the universal comparison, then for every \(k\),
\[
f(2/m)\le f\bigl(\Pr_{G_k}(x^3=1)\bigr)\le\Pr_{G_k}([x,y,y]=1).
\]
Letting \(k\to\infty\) proves \(f(2/m)\le1/m\). It also shows that the ratio of the two probabilities tends to \(1/2\). This completes the proof.

## Verification

A standalone standard-library Python script `verify_engel.py` exhaustively enumerates the elements, products, commutators, nested commutators and cubes in nine scalar semidirect products with prime-field orders \(q=7,13,19\) and complement orders divisible by \(3\). Every tested count agrees with the exact two formulas. The general argument does not depend on the finite checks; in particular the infinite limit is justified by the explicit prime-power construction and the monotonicity inequality.

## Relationship to prior work

Putignano and Vannacci, *Comparing word probabilities in finite groups* (arXiv:2610.23100v1, first public October 16, 2026), prove existence of a nondecreasing positive comparison function for the cubic word and the 2-Engel word (their Proposition 1). They do not give these pointwise upper obstructions in their treatment of this comparison. The general structure of Engel digraphs of abelian-kernel cyclic Frobenius groups has also been determined independently in earlier work; the computation of the 2-Engel probability alone is therefore not asserted as a new theorem. The contribution here is the exact coupling with cubic-word probability, together with the resulting **universal comparison-function obstruction at every \(2/m\) with \(3\mid m\)**.

## Limitations

The upper bounds on universal comparison functions are *necessary*, not claimed sufficient. They do not establish the existence of an optimal comparison function with equality at the specified points, nor a universal linear bound. The formulas require a fixed-point-free cyclic complement and an abelian kernel; beyond that family no groupwise exact formula is asserted. Coverage in unindexed word-probability literature is a remaining originality risk.

## References

1. L. Putignano and M. Vannacci, *Comparing word probabilities in finite groups*, arXiv:2610.23100v1 (first public October 16, 2026), especially Section 2 and Proposition 1. https://arxiv.org/abs/2610.23100
2. *Engel digraphs of abelian-kernel cyclic Frobenius groups*, publicly indexed mathematical research record, October 2026 (structural comparison; used only for previously known Engel-digraph coverage).
