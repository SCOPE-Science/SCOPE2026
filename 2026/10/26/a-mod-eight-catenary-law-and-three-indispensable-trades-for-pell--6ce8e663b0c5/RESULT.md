# A mod-eight catenary law and three indispensable trades for Pell-triple semigroups

## Finding
Fix integers \(u\ge1\) and odd \(i\ge5\), and define \(P_0(u)=0\), \(P_1(u)=1\), and \(P_{n+2}(u)=uP_{n+1}(u)+P_n(u)\). Set
\[
a=P_i(u),\quad b=P_{i+2}(u),\quad c=P_{i+4}(u),\qquad S=\langle a,b,c\rangle.
\]
Write \(q=u^2+2\), \(Q=\lfloor a/q\rfloor\), and \(r=a-qQ\). In the factorization coordinates \((x,y,z)\in\mathbb N_0^3\), where the represented integer is \(xa+yb+zc\), a minimal presentation of \(S\) consists of exactly these three indispensable trades:
\[
\begin{aligned}
(b-Q,0,0)&\longleftrightarrow(0,r,Q),\\
(0,q,0)&\longleftrightarrow(1,0,1),\\
(0,0,Q+1)&\longleftrightarrow(b-Q-1,q-r,0).
\end{aligned}
\]
Their degrees are three distinct Betti elements; each Betti fiber has exactly the displayed pair of factorizations. Under the usual distance between factorizations, the catenary degree is
\[
\boxed{\mathsf c(S)=b-Q+q-r-1=\begin{cases}
b-Q+q-2,&i\equiv1,7\pmod8,\\
b-Q,&i\equiv3,5\pmod8.
\end{cases}}
\]

## Assumptions and scope
The theorem covers all integer parameters \(u\ge1\) and odd \(i\ge5\), with no upper bound. The embedding dimension is exactly three. A factorization of \(s\in S\) is \(v=(x,y,z)\in\mathbb N_0^3\) satisfying \(xa+yb+zc=s\). For two factorizations, let \(g\) be their componentwise minimum and set \(d(v,w)=\max\{\lVert v-g\rVert_1,\lVert w-g\rVert_1\}\). The catenary degree is the least \(N\) such that every pair of factorizations of every element can be joined through factorizations of that element by a chain with pairwise distances at most \(N\). A presentation is a set of replacement trades connecting every such fiber; it is minimal if no trade can be removed.

## Proof
**Arithmetic preliminaries.** The recurrence twice gives \(c=qb-a\). The standard consecutive-index determinant gives \(\gcd(P_i(u),P_{i+2}(u))=\gcd(P_i(u),u)=1\) for odd \(i\), since \(P_i(u)\equiv1\pmod u\). For \(i\ge5\), direct monotonicity and the recurrence give \(a>q\) and \(b>2a\). These imply \(Q\ge1\), \(1\le r<q\), and all coordinates of the three claimed trades are nonnegative. The odd-index subsequence \(A_j=P_{2j+1}(u)\) satisfies \(A_{j+2}=qA_{j+1}-A_j\), with \(A_0=1\), \(A_1=q-1\). Thus \(A_j\pmod q\) repeats \(1,-1,-1,1\), yielding the stated mod-eight classification \(r\in\{1,q-1\}\). Every trade preserves its represented integer by \(a=qQ+r\) and \(c=qb-a\).

**Completeness of the presentation.** Start with an arbitrary factorization \((x,y,z)\). Apply the second trade from \(qb\) to \(a+c\) until \(0\le y<q\). Whenever \(z\ge Q+1\), replace \((Q+1)c\) using the third trade. This increases \(y\) by \(q-r<q\); at most one replacement \(qb\to a+c\) restores \(y<q\). Combined, these steps decrease \(z\) by at least \(Q\ge1\), so they terminate with \(z\le Q\). If \(z=Q\) and \(y\ge r\), apply the first trade to replace \(rb+Qc\) by \((b-Q)a\). The resulting canonical factorization satisfies either \(0\le z<Q\), \(0\le y<q\), or \(z=Q\), \(0\le y<r\). There are precisely \(qQ+r=a\) permissible pairs \((y,z)\), with \(t=y+qz\) taking each integer from \(0\) to \(a-1\) once. Since \(c\equiv qb\pmod a\) and \(\gcd(a,b)=1\), a represented integer determines \(t\pmod a\), hence its unique canonical \((y,z)\) and then its unique \(x\). Consequently all same-element factorizations are connected using the three trades.

**Exactly two factorizations at each critical degree.** Denote the displayed trade degrees by \(E_A=(b-Q)a=rb+Qc\), \(E_B=qb=a+c\), and \(E_C=(Q+1)c=(b-Q-1)a+(q-r)b\). They are distinct: \(E_A<E_C\) because \(E_C-E_A=b(q-r)-a>0\), and \(E_B<E_A\), since \(a-q\ge Q\) and \(b>a\) imply \((b-Q)a-qb=b(a-q)-Qa>0\). For \(E_B\), the inequality \(2c>qb\) forces \(z\in\{0,1\}\); coprimality and \(q<a\) give exactly \((0,q,0)\) and \((1,0,1)\). For \(E_A\), the inequality \(E_A<E_C\) forces \(z\le Q\). Writing \(d=b-Q-x\) in any factorization gives \((d+z)a=(y+qz)b\), with \(0\le d+z\le b\). Coprimality gives either the original pure-\(a\) factorization or \(d+z=b\), forcing \(z=Q\), \(y=r\), \(x=0\). For \(E_C\), if \(z\ge Q+1\) the pure-\(c\) factorization is forced. Otherwise put \(t=Q+1-z\), so \(1\le t\le Q+1\), and \((qt-y)b=(x+t)a\). The right side is positive, so coprimality forces \(qt-y=ka\) with \(k\ge1\). Since \(qt\le a+q-r<2a\), necessarily \(k=1\), \(t=Q+1\), \(z=0\), \(y=q-r\), \(x=b-Q-1\). Each pair has disjoint coordinate support, and hence its trade cannot be omitted from any presentation. The three trades form a minimal presentation and the three degrees are precisely the Betti elements.

**Exact catenary degree.** The three pairwise distances of the displayed trades are respectively \(\max\{b-Q,r+Q\}\), \(q\), and \(\max\{Q+1,b-Q-1+q-r\}\). From \(b>2a\), \(a=qQ+r\), and \(q\ge3\), all are at most \(D=b-Q-1+q-r\), and the third distance equals \(D\). Since the three trades connect every fiber, \(\mathsf c(S)\le D\). The fiber of \(E_C\) contains only its two factorizations, so any chain between them must jump by distance \(D\); therefore \(\mathsf c(S)\ge D\). This proves the theorem.

## Verification
The accompanying standalone script `pell_catenary_verify.py` tests \(64\) parameter pairs, enumerates both complete factorizations of \(34\) critical fibers with degree below one million, and checks connectivity for every represented integer through \(1200\) in three smaller examples. It also checks the recurrence relations, three trades, and formula at all \(64\) sample parameter pairs. The script uses exact integer arithmetic. These are finite corroborations, not a substitute for the preceding proof.

Sample output gives \((u,i;a,b,c;q,Q,r;\mathsf c(S))=(1,5;5,13,34;3,1,2;12)\) and \((1,7;13,34,89;3,4,1;31)\).

## Relationship to prior work
Komatsu and Mu, *\(p\)-numerical semigroups of Pell triples* (first public preprint 18 July 2023), investigate this Pell-triple family through generalized Frobenius numbers and genera; the available full preprint does not state the three indispensable trades or a catenary formula. Aguiló-Gost and García-Sánchez (2010) provide a general three-generator factorization/tessellation algorithm for computing catenary degree, covering individual instances but not stating this arithmetic two-branch, all-parameter Pell formula or the explicit factorization fibers. Süer and Sezgin study telescopic families, unlike this pairwise-coprime three-generator family. The result uses elementary factorization moves rather than claiming a general method for arbitrary semigroups.

## Limitations
The result applies only to the specified odd-index Pell triples separated by two and four recurrence steps; it does not claim all Pell triples or even starting indices. The prior general three-generator algorithms can evaluate fixed instances; the distinct asserted contribution is the explicit uniform family classification and minimal presentation. No claim of exhaustive literature uniqueness, independent validation, or universal result for other recurrence triples is made.

## References
- T. Komatsu and J. Mu, *\(p\)-numerical semigroups of Pell triples*, arXiv:2307.08998 (first public 2023-07-18), https://arxiv.org/abs/2307.08998.
- F. Aguiló-Gost and P. A. García-Sánchez, *Factoring in Embedding Dimension Three Numerical Semigroups*, Electronic Journal of Combinatorics 17 (2010), R138, DOI:10.37236/410.
- M. Süer and M. Ş. Sezgin, *Betti elements and catenary degree of telescopic numerical semigroup families*, arXiv:2011.09548 (2020).

