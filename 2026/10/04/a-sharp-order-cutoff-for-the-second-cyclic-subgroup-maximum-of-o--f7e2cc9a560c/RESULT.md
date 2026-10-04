# A sharp order cutoff for the second cyclic-subgroup maximum of odd prime-power groups

## Finding

Let \(p\) be an odd prime and let \(n\ge3\). For a finite group \(G\), write \(C(G)\) for the set of cyclic subgroups of \(G\). Define
\[
M_{p,n}
=
\frac{2p^{n-1}-p^{n-2}+p-2}{p-1}.
\]

Among all **regular** \(p\)-groups \(G\) of order \(p^n\), the largest value of \(|C(G)|\) strictly below the exponent-\(p\) maximum is exactly
\[
\boxed{|C(G)|=M_{p,n}.}
\]
Equality holds precisely when
\[
\exp(G)=p^2
\qquad\text{and}\qquad
[G:\Omega_1(G)]=p.
\]

Consequently, if
\[
3\le n\le p,
\]
then every group of order \(p^n\) is regular, and therefore
\[
\boxed{
M_{p,n}
}
\]
is the actual second maximum of the number of cyclic subgroups among **all** groups of order \(p^n\).

The cutoff \(n\le p\) is sharp. For the regular wreath product
\[
W=C_p\wr C_p
\]
of order \(p^{p+1}\),
\[
\Omega_1(W)=W,
\qquad
\exp(W)=p^2,
\]
and
\[
\boxed{
|C(W)|
=
\frac{p^{p-2}(3p^2-3p+1)+p-2}{p-1}
=
M_{p,p+1}+p^{p-2}(p-1).
}
\]
Thus
\[
|C(W)|>M_{p,p+1}.
\]

For \(p\ge5\), this completely settles the initial order range \(3\le n\le p\) of the 2020 open second-maximum problem and shows that its exceptional branch cannot occur before order \(p^{p+1}\).

## Assumptions and scope

For a finite \(p\)-group \(G\), put
\[
\Omega_{\{1\}}(G)=\{x\in G:x^p=1\}
\]
and
\[
\Omega_1(G)=\langle\Omega_{\{1\}}(G)\rangle.
\]

A standard theorem of P. Hall says that in a regular \(p\)-group, the elements of order dividing \(p\) form the subgroup \(\Omega_1(G)\). Hence
\[
\Omega_{\{1\}}(G)=\Omega_1(G)
\]
for regular \(p\)-groups. Hall's regularity theory also gives that every finite \(p\)-group of nilpotency class strictly less than \(p\) is regular.

Lazorec, Shen, and Tărnăuceanu proved the relevant upper bound for odd-prime \(p\)-groups satisfying
\[
\exp(G)\ne p
\qquad\text{and}\qquad
\Omega_1(G)\ne G,
\]
and left the case
\[
p\ge5,
\qquad
\Omega_1(G)=G
\]
as an open problem.

The statement here identifies a broad structural region in which that exceptional case is impossible, obtains the exact second maximum there, and proves the order cutoff sharp by an explicit wreath-product calculation.

## Proof

The global maximum is attained by groups of exponent \(p\). Indeed, if \(|G|=p^n\) and \(\exp(G)=p\), every nonidentity cyclic subgroup has order \(p\), so
\[
|C(G)|
=
1+\frac{p^n-1}{p-1}
=
\frac{p^n+p-2}{p-1}.
\]

Now let \(G\) be a regular \(p\)-group of order \(p^n\) with
\[
\exp(G)\ne p.
\]
Because regularity gives
\[
\Omega_{\{1\}}(G)=\Omega_1(G),
\]
the equality
\[
\Omega_1(G)=G
\]
would imply that every element of \(G\) has order dividing \(p\), contradicting \(\exp(G)\ne p\). Therefore
\[
\Omega_1(G)\ne G.
\]

Theorem 3.1 of Lazorec, Shen, and Tărnăuceanu now applies. Their proof gives
\[
|C(G)|
\le
\frac{p^n+p^2-p-1+(p-1)^2c_1(G)}{p^2-p},
\]
where
\[
c_1(G)
=
\frac{|\Omega_{\{1\}}(G)|-1}{p-1}.
\]
Since \(\Omega_1(G)\ne G\),
\[
|\Omega_{\{1\}}(G)|
\le
|\Omega_1(G)|
\le
p^{n-1}.
\]
Substitution yields
\[
|C(G)|
\le
\frac{2p^{n-1}-p^{n-2}+p-2}{p-1}
=
M_{p,n}.
\]

Their equality analysis says that equality holds exactly when
\[
\exp(G)=p^2
\]
and
\[
\Omega_{\{1\}}(G)=\Omega_1(G)
\]
has index \(p\) in \(G\). In the regular setting the set-subgroup equality is automatic, so the equality condition reduces to
\[
\exp(G)=p^2
\qquad\text{and}\qquad
[G:\Omega_1(G)]=p.
\]

The bound is attained for every \(n\ge3\). For example,
\[
G=C_{p^2}\times C_p^{\,n-2}
\]
is regular, has exponent \(p^2\), and its subgroup of elements killed by \(p\) has order \(p^{n-1}\).

This proves the exact second maximum among regular groups.

Next suppose
\[
3\le n\le p.
\]
A \(p\)-group of order \(p^n\) has nilpotency class at most \(n-1\), so
\[
\operatorname{cl}(G)\le n-1<p.
\]
By Hall's theorem, \(G\) is regular. Therefore the regular-group result just proved applies to every group of order \(p^n\), giving the actual second maximum \(M_{p,n}\).

It remains to prove that the cutoff is sharp.

Let
\[
W=C_p\wr C_p
=
V\rtimes\langle\sigma\rangle,
\qquad
V\cong C_p^p,
\]
where \(\sigma\) cyclically permutes the \(p\) coordinates of \(V\). Write elements as
\[
(v,\sigma^j),
\qquad
v\in\mathbf F_p^p,
\qquad
j\in\mathbf F_p.
\]

If
\[
j=0,
\]
then every nonidentity element has order \(p\).

If
\[
j\ne0,
\]
then
\[
(v,\sigma^j)^p
=
\left(
v+\sigma^jv+\cdots+\sigma^{(p-1)j}v,
1
\right).
\]
Because \(j\ne0\), the powers of \(\sigma^j\) run through all cyclic coordinate shifts. Hence
\[
v+\sigma^jv+\cdots+\sigma^{(p-1)j}v
=
\left(\sum_{k=1}^{p}v_k\right)(1,\ldots,1).
\]
Therefore \((v,\sigma^j)\) has order \(p\) exactly when
\[
\sum_{k=1}^{p}v_k=0,
\]
and otherwise it has order \(p^2\).

For each nonzero \(j\), exactly \(p^{p-1}\) vectors \(v\) have coordinate sum zero. Thus the number of solutions of
\[
x^p=1
\]
in \(W\), including the identity, is
\[
s
=
p^p+(p-1)p^{p-1}
=
p^{p-1}(2p-1).
\]
The remaining
\[
p^{p+1}-s
\]
elements have order \(p^2\).

Since a cyclic subgroup of order \(p\) has \(p-1\) generators and one of order \(p^2\) has \(p(p-1)\) generators,
\[
|C(W)|
=
1+\frac{s-1}{p-1}
+\frac{p^{p+1}-s}{p(p-1)}.
\]
Substituting \(s=p^{p-1}(2p-1)\) gives
\[
|C(W)|
=
\frac{p^{p-2}(3p^2-3p+1)+p-2}{p-1}.
\]
On the other hand,
\[
M_{p,p+1}
=
\frac{p^{p-1}(2p-1)+p-2}{p-1}.
\]
The difference is
\[
|C(W)|-M_{p,p+1}
=
p^{p-2}(p-1)>0.
\]

Finally, \(W\) is generated by the top element \(\sigma\) and a standard basis vector of \(V\), both of order \(p\), so
\[
\Omega_1(W)=W.
\]
The above order computation exhibits elements of order \(p^2\), so
\[
\exp(W)=p^2.
\]
Thus the exceptional branch occurs already at order \(p^{p+1}\), proving that the order cutoff is sharp.

## Verification

The included replay checks all algebraic simplifications in the theorem and independently enumerates the wreath product for \(p=3\) and \(p=5\).

For each tested prime it constructs
\[
C_p^p\rtimes C_p
\]
with the cyclic-shift action, computes the order of every element directly by repeated group multiplication, reconstructs \(|C(W)|\) from the resulting element-order distribution, and verifies the closed formula.

For \(p=3\), the replay obtains
\[
|C(C_3\wr C_3)|=29,
\]
matching the explicit example recorded in the 2020 source.

For \(p=5\), it checks all \(5^6=15625\) elements and obtains the predicted value
\[
|C(C_5\wr C_5)|=1907.
\]

The replay also enumerates small abelian equality examples
\[
C_{p^2}\times C_p^{\,n-2}
\]
and confirms that their cyclic-subgroup counts equal \(M_{p,n}\).

The finite checks do not prove the universal regularity or extremal statements; those follow from Hall's regularity theorem and Theorem 3.1 of the cited 2020 source.

## Relationship to prior work

Lazorec, Shen, and Tărnăuceanu determine the second maximum under the assumption
\[
\Omega_1(G)\ne G
\]
and state the equality condition used above. They then explicitly isolate
\[
p\ge5,
\qquad
\Omega_1(G)=G
\]
as the remaining open case. They observe inside their discussion that class-two groups cannot supply the missing examples.

Hall's regular \(p\)-group theory is much broader than the class-two observation: in a regular \(p\)-group the elements killed by \(p\) already form \(\Omega_1(G)\), and every group of class less than \(p\) is regular. Combining this with the 2020 extremal theorem removes the entire regular region from the open branch.

The additional wreath-product calculation shows that the resulting order cutoff is not an artifact of the proof. The first order at which regularity is no longer forced,
\[
p^{p+1},
\]
already contains a group generated by elements of order \(p\), of exponent \(p^2\), whose number of cyclic subgroups strictly exceeds the regular second-maximum value.

Targeted searches for the second cyclic-subgroup maximum in regular \(p\)-groups, the \(\Omega_1(G)=G\) branch, and the cyclic-subgroup count of \(C_p\wr C_p\) did not locate this combined sharp-cutoff statement or the displayed general wreath-product count.

## Limitations

The result does not determine the second maximum once
\[
n\ge p+1.
\]
The wreath product provides a strict lower bound for the unresolved value at the first possible order, but no claim is made that it is extremal there.

The regularity theorem is classical; the new content is the sharp extremal consequence for the 2020 problem together with the exact boundary calculation showing that the order range cannot be extended.

An equivalent observation or wreath-product count may exist under different terminology or in unindexed literature. Failed searches are not a proof of novelty.

## References

1. M.-S. Lazorec, R. Shen, and M. Tărnăuceanu, “The second minimum/maximum value of the number of cyclic subgroups of finite \(p\)-groups,” arXiv:2001.10521, first public version 28 January 2020; *Bulletin of the Australian Mathematical Society* 103 (2021), 96–103, DOI 10.1017/S0004972720000337.
2. P. Hall, “A contribution to the theory of groups of prime-power order,” *Proceedings of the London Mathematical Society* (2) 36 (1934), 29–95, DOI 10.1112/plms/s2-36.1.29.
3. M. Hall, *The Theory of Groups*, Macmillan, 1959.
