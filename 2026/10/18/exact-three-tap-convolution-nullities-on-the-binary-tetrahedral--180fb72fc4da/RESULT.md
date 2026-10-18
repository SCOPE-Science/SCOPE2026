# Exact three-tap convolution nullities on the binary tetrahedral group

## Finding

Let \(G=2T\cong\mathrm{SL}(2,3)\) be the group of 24 Hurwitz unit quaternions, let \(Q=\{\pm1,\pm i,\pm j,\pm k\}\triangleleft G\), and let \(S\subset G\) contain exactly three distinct elements. The unweighted left-convolution operator on \(\mathbb C[G]\) is
\[
(T_S f)(h)=\sum_{s\in S}f(s^{-1}h).
\]
It is singular **if and only if** \(S\) meets each of the three cosets of \(Q\) in exactly one point. For such a transversal, all three edge differences \(s_i^{-1}s_j\), \(i<j\), have order three or six. Let \(m(S)\) count the differences of order three. Then the exact complex nullity and the complete support census are:

| \(m(S)\) | \(\dim_{\mathbb C}\ker T_S\) | Number of unordered three-element supports |
| ---: | ---: | ---: |
| 3 | 16 | 32 |
| 2 | 2 | 288 |
| 1 | 8 | 96 |
| 0 | 6 | 96 |
| not a transversal | 0 | 1512 |

In particular, there are exactly 512 singular supports out of \(\binom{24}{3}=2024\). The maximum nullity 16 is attained precisely by the 32 left cosets of the four subgroups of order three. The nullity-eight cases are precisely the remaining transversal subsets of cosets of the four order-six subgroups. The two noncyclic transversal types have nullity two or six, distinguished by whether exactly two or zero edge differences have order three.

## Assumptions and scope

The quaternion elements have unit norm, and multiplication uses \(i^2=j^2=k^2=ijk=-1\). Explicitly,
\[
G=\{\pm1,\pm i,\pm j,\pm k\}\;\cup\;
\left\{\frac{\varepsilon_0+\varepsilon_1i+\varepsilon_2j+\varepsilon_3k}{2}:\varepsilon_r\in\{-1,1\}\right\}.
\]
All ranks and kernels are over \(\mathbb C\); coefficients of the three taps are exactly \(+1\), not arbitrary weights. Repeated support points, other finite groups, weighted convolutions, and nonconsecutive support sizes are outside the assertion. A change \(S\mapsto gS\) multiplies the convolution operator by the invertible left-translation \(L_g\) and does not change nullity.

For a normalized support \(S=\{1,x,y\}\), write \(a=\operatorname{Re}x\), \(b=\operatorname{Re}y\), and \(c=\operatorname{Re}(x^{-1}y)\). If \(S\) is a transversal, each of \(a,b,c\) is \(\pm\tfrac12\). A negative value means that corresponding edge element has order three; a positive value means order six.

## Proof

### The complete list of Fourier blocks

Choose \(t=(-1+i+j+k)/2\), which has order three. Then \(G=Q\rtimes\langle t\rangle\), and \(G/Q\cong C_3\). Let \(\omega=\exp(2\pi i/3)\) and \(\chi_j(t)=\omega^j\), \(\chi_j(Q)=1\), \(j=0,1,2\). The irreducible representations of \(G\) consist of these three characters; the three two-dimensional representations \(\chi_j\rho\), where \(\rho:G\hookrightarrow\mathrm{SU}(2)\) is the faithful quaternion representation; and the irreducible three-dimensional tetrahedral-rotation representation \(R:G\to\mathrm{SO}(3)\) with kernel \(\{\pm1\}\). Their squared degrees sum to \(3+12+9=24\), so this list is complete. By finite-group Fourier decomposition,
\[
\dim\ker T_S
=\sum_{\pi\in\widehat G}(\dim\pi)\,
\dim\ker\!\left(\sum_{s\in S}\pi(s)\right).
\]
Left-normalize \(S\) to \(\{1,x,y\}\). The nontrivial one-dimensional blocks vanish exactly when the quotient classes of \(1,x,y\) are all distinct; in this case the two blocks each contribute one to nullity.

### The quaternionic two-dimensional blocks

For a unit quaternion \(z\), \(\operatorname{tr}\rho(z)=2\operatorname{Re}z\). For \(u,v\in\mathbb C\), the \(2\times2\) determinant identity is
\[
\det\bigl(I+u\rho(x)+v\rho(y)\bigr)
=1+u^2+v^2+2ua+2vb+2uvc. \tag{1}
\]
It follows from \(\det\rho(x)=\det\rho(y)=1\), together with \(\operatorname{tr}\rho(x^{-1}y)=2c\). For the untwisted block, (1) is \(3+2(a+b+c)\). Direct quaternion multiplication shows that \(a+b+c\ge-1\) whenever \(x,y\) are not in opposite nonidentity quotient cosets. For opposite cosets it is zero exactly when \(a=b=c=-1/2\), i.e., \(m(S)=3\). In that case \(y=x^{-1}\) and \(x^3=1\), so \(I+\rho(x)+\rho(x)^2=0\): the entire two-dimensional block vanishes, contributing four to regular-representation nullity.

For a nontrivial character twist, if \(x\in Q\setminus\{1\}\) and \(y\notin Q\), set \(u=1\), \(v\in\{\omega,\omega^2\}\). Formula (1) becomes \(1+2a+v(2(b+c)-1)\), which is nonzero because \(a\in\{-1,0\}\) and \(1,v\) are linearly independent over \(\mathbb R\). If \(x,y\notin Q\) belong to the same quotient coset, \(u=v\in\{\omega,\omega^2\}\) and the determinant is
\[
-(1+2c)+2u(a+b-1-c),
\]
which cannot vanish because \(c\in\{-1,0\}\). With both elements in \(Q\), all twists coincide with the already invertible untwisted block.

For opposite nontrivial quotient cosets, \(u=\omega\), \(v=\omega^2\), or vice versa, and (1) becomes \(2(\omega a+\omega^2 b+c)\) up to conjugation. It vanishes exactly when \(a=b=c\). Thus both nontrivially twisted two-dimensional blocks have one-dimensional kernels when \(m(S)=3\) or \(m(S)=0\), and are invertible otherwise. The blocks are not zero matrices, by taking traces; each singular twisted block therefore contributes two to the regular nullity. In the \(m(S)=3\) case this can also be read from the eigenvalues \(\omega,\omega^2\) of \(\rho(x)\).

### The tetrahedral three-dimensional block

The image \(R(Q)\) is the Klein four group of diagonal matrices with diagonal signs whose product is one. The image of \(t\) cyclically permutes the three coordinate axes. If \(x,y\in Q\), the matrix \(I+R(x)+R(y)\) is diagonal with entries in \(\{-1,1,3\}\). If one element belongs to \(Q\) and the other to a nonidentity quotient coset, its determinant equals \(1\) or \(9\). If both lie in the same nonidentity quotient coset, the determinant is likewise \(1\) or \(9\). In particular, none of these cases is singular.

If \(x,y\) occupy the two different nonidentity quotient cosets, let \(P\) be the three-cycle permutation matrix and write \(R(x)=DP\), \(R(y)=EP^2\), where \(D,E\) are diagonal sign matrices of determinant one. Writing their diagonal entries as \(d_i,e_i\), direct expansion gives
\[
\det(I+DP+EP^2)
=3-(e_1d_2+e_2d_3+e_3d_1)\in\{0,4\}. \tag{2}
\]
The determinant is zero exactly when \(R(y)=R(x)^{-1}\), equivalently \(xy\in\{\pm1\}\). Then \(I+R(x)+R(x)^2\) is three times the projection onto the one-dimensional rotation axis; hence the block has kernel dimension two and contributes six to regular nullity.

For unit quaternions with real parts \(a,b,c\in\{\pm1/2\}\), the equality \(xy\in\{\pm1\}\) holds exactly when the edge-order pattern is \((3,3,3)\) or \((3,6,6)\). Indeed, write \(x=a+\mathbf u\), \(y=b+\mathbf v\). Then \(|\mathbf u|=|\mathbf v|=\sqrt3/2\) and \(c=ab+\mathbf u\cdot\mathbf v\); equality in Cauchy--Schwarz forces \(\mathbf v=\pm\mathbf u\), which gives precisely these two patterns. Conversely these patterns force equality. Combining all Fourier blocks gives the four stated nullities and proves invertibility for every nontransversal.

### Exhaustive support counts

Each quotient coset has eight elements, so the number of transversals is \(8^3=512\). To count their edge patterns, normalize the unique element in \(Q\) to the identity. There are eight choices for that element and \(8\times8=64\) normalized ordered pairs \((x,y)\) with \(x\in Qt\), \(y\in Qt^2\). Exactly four elements in \(Qt\) have order three and four have order six. Conjugation by \(Q\) is transitive within each class, so inspecting \(x=t\) and \(x=-t\) suffices. Multiplication with the eight elements \(y\in Qt^2\) yields:

| Order of \(x\) | \((3,3,3)\) | \((3,3,6)\) | \((3,6,6)\) | \((6,6,6)\) |
| --- | ---: | ---: | ---: | ---: |
| 3 | 1 | 6 | 1 | 0 |
| 6 | 0 | 3 | 2 | 3 |

Multiplying both rows by four gives normalized-pair counts \((4,36,12,12)\). Multiplying again by eight gives the table's support counts \((32,288,96,96)\). Among the other \(2024-512=1512\) supports, every convolution is invertible. The four order-three subgroups each have eight left cosets, yielding the 32 nullity-16 supports; the 96 nullity-eight supports are the other cyclic transversals in the four order-six subgroups' cosets.

## Verification

Run `python3 check_hurwitz_census.py` with Python 3 and its standard library only. The checker constructs all 24 units with doubled integer coordinates and verifies exact quaternion multiplication, the quotient cosets, the normalized-pair edge-order table, and the nullity of each of the \(\binom{23}{2}=253\) identity-containing three-point supports. Ranks are computed with fraction-free integer elimination, with every division checked for exactness. Translation invariance and the three choices of normalizing element establish that these 253 checks cover all \(\binom{24}{3}=2024\) supports. The independently computed nullity census agrees with the proof:
\[
\#\{S:\dim\ker T_S=0,2,6,8,16\}
=(1512,288,96,96,32).
\]
The Fourier-block argument independently proves that these are the only possibilities; the checker is an exact exhaustive consistency certificate, not a substitute for the representation-theoretic proof.

## Relationship to prior work

Dechant (2012) gives the Hurwitz-quaternion realization of the binary tetrahedral group, including its connection to the \(D_4\) root system. Arezoomand and Taeri (2013) prove general finite-Cayley representation-block formulas for spectra and kernels. Those results establish the group model and the Fourier decomposition used above; their inspected arguments do not state the transversal-only singularity criterion, four-tier nullity classification, or all-support census on this group. Other three-tap classifications for dicyclic, elementary generalized dihedral, and ternary Heisenberg families treat nonisomorphic groups and do not imply this exact classification through their hypotheses. Conversely, the present theorem does not extend their conclusions to other finite groups.

## Limitations

The classification concerns the fixed unweighted coefficient triple on one finite group. It does not cover weighted taps, other support sizes, other binary polyhedral groups, or spectra away from eigenvalue zero. The historical sources support the representation method and group geometry, not priority for these explicit nullity counts. An undiscovered equivalent in older Cayley digraph or group-algebra literature remains a possibility. No independent mathematical audit or publication-priority certification has been performed.

## References

1. P.-P. Dechant, *Clifford Algebra Unveils a Surprising Geometric Significance of Quaternionic Root Systems of Coxeter Groups*, arXiv:1205.1451 (first posted 2012-05-07), especially Sections 3 and 6. https://arxiv.org/abs/1205.1451
2. M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of \(n\)-Cayley Digraphs*, Electronic Journal of Combinatorics **20** (2013), #P57, particularly Lemma 1 and Corollary 7. https://doi.org/10.37236/3105
