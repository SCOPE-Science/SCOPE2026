# Cyclically symmetric minimum-genus orientable embedding of K(4,10)

Let A={a0,a1,a2,a3} and B={b0,...,b9}. The orientable genus of K(4,10) is

g = ceil((4-2)(10-2)/4)=4.

Define phi=(a0 a1). Consider the following rotation system (indices on B are mod 10):

- rot(b_i)=(a0,a2,a1,a3) for even i and (a1,a2,a0,a3) for odd i;
- rot(a0)=(0,1,2,3,4,5,6,7,8,9);
- rot(a1)=(1,2,3,4,5,6,7,8,9,0);
- rot(a2)=rot(a3)=(0,9,8,7,6,5,4,3,2,1).

Independent successor-rule face tracing gives exactly 20 faces, all of length 4. Thus

V-E+F = 14-40+20 = -6 = 2-2g,

so the embedding has genus 4 and is minimum-genus.

Now define g(a_j)=a_{phi(j)} and g(b_i)=b_{i+1}. On each B-vertex, applying phi to the listed cyclic order sends the even pattern to the odd pattern and vice versa. On each A-vertex, adding 1 to every B-label sends the listed cyclic order to the target row up to cyclic rotation. Therefore g is an orientation-preserving automorphism of the rotation system. Its action on B is a 10-cycle, so g has order 10.

Hence K(4,10) admits a minimum-genus orientable quadrangulation with an orientation-preserving automorphism of order 10 acting cyclically on the 10-vertex part.

## Reproducibility and limitations

The explicit witness above is sufficient for the claim and was independently traced and symmetry-checked in the 2026-09-29 audit. The previously referenced files `output/artifacts/verification.json`, `verify_witness.py`, and `enumerate.py` are not present in the audited repository tree. Consequently the former supporting census of 5896 symmetric rotation systems is not part of this repaired finding.

No uniqueness, classification of all symmetric embeddings, or statement about nonorientable embeddings is claimed.

## References

- Jones, *Regular embeddings of complete bipartite graphs: classification and enumeration*, arXiv:0911.4340.
- Fan and Li, *The complete bipartite graphs with a unique edge-transitive embedding*, J. Graph Theory 87 (2018).
- Flapan et al., *Symmetries of Embedded Complete Bipartite Graphs*, arXiv:1205.4052 (spatial-embedding category, cited for contrast).
